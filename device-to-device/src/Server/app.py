#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
import requests
import logging
import sys
import sched, time

app = Flask(__name__)
# id, device, message, done
messages = []
message_scheduler = sched.scheduler(time.time, time.sleep)
failed_messages = []
sent_messages = []

# ip
devices = []
currentID = 0

def ping_device(message_index):
    message = messages[message_index]
    try:
        response = requests.post('http://' + message['target_device']['ip'] + '/api/messages', json = message)
    except:
        print('Error', file=sys.stderr)
        failed_messages.append(messages.pop(message_index))
    else:
        sent_messages.append(messages.pop(message_index))



def send_messages():
    for idx, message in enumerate(messages):
        ping_device(idx)


@app.route('/api/devices', methods=['GET'])
def get_devices():
    return jsonify({'devices': devices})

@app.route('/api/devices/<device_ip>', methods=['GET'])
def get_device(device_ip):
    device = [device for device in devices if device['ip'] == device_ip]
    if len(device) == 0:
        abort(404)
    return jsonify({'device': device[0]})

@app.route('/api/devices', methods=['POST'])
def create_device():
    if not request.json or not 'ip' in request.json:
        abort(400)
    device = {
        'device_id': len(devices) + 1,
        'ip': request.json['ip']
    }
    devices.append(device)
    return jsonify({'device': device}), 201

@app.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages})

@app.route('/api/messages/<int:message_id>', methods=['GET'])
def get_message(message_id):
    message = [message for message in messages if message['id'] == message_id]
    if len(message) == 0:
        abort(404)
    return jsonify({'message': message[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/messages', methods=['POST'])
def create_message():
    global currentID
    if not request.json or not 'target_device' in request.json:
        abort(400)
    currentID += 1
    message = {
        'id': currentID,
        'origin_device': {'ip': request.remote_addr, 'device_id': request.json['device_id']},
        'target_device': request.json['target_device'],
        'message': request.json['message'],
        'repeated_sends': 0
    }
    messages.append(message)
    send_messages()
    return jsonify({'message': message}), 201

@app.route('/api/messages/<int:message_id>', methods=['PUT'])
def update_message(message_id):
    message = [message for message in messages if message['id'] == message_id]
    if len(message) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'message' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    message[0]['message'] = request.json.get('message', message[0]['message'])
    message[0]['done'] = request.json.get('done', message[0]['done'])
    return jsonify({'message': message[0]})

@app.route('/api/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = [message for message in messages if message['id'] == message_id]
    if len(message) == 0:
        abort(404)
    messages.remove(message[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
