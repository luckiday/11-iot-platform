import requests
import argparse
import sys

from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

serverIP = '192.168.10.20:5000'
currentIP = '192.168.10.20:5001'

parser = argparse.ArgumentParser()

parser.add_argument('--deviceID', help='Please select a device from the list')
parser.add_argument('--message', help='Please send a message to device')

args = parser.parse_args()

available_devices = []
messages = []
failed_messages = []

@app.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages})

@app.route('/api/messages', methods=['POST'])
def create_message():
    if not request.json or not 'device' in request.json:
        abort(400)

    message = {
        'id': request.json['id'],
        'origin_device': request.json['device'],
        'message': request.json['message'],
        'done': False
    }
    messages.append(message)
    return jsonify({'message': message}), 201

def ping_server():
    deviceRequest = requests.get('http://' + serverIP + '/api/devices/' + currentIP)
    if 'device' in deviceRequest.json():
        print('Device exists in server', file=sys.stderr)
    else:
        device = {'ip' : currentIP}
        deviceRequest = requests.post('http://' + serverIP + '/api/devices', json = device)

    return deviceRequest

def get_devices():
    deviceRequest = requests.get('http://' + serverIP + '/api/devices')
    return deviceRequest.json()

def send_message(target_ip, message):
    ping_server()
    available_devices = get_devices()['devices']
    print(available_devices, file=sys.stderr)
    device = [device for device in available_devices if device['ip'] == target_ip]
    if not device:
        print('Target Device does not exist', file=sys.stderr)
        return
    message = {'device' : device[0], 'message': message}
    messageRequest = requests.post('http://' + serverIP + '/api/messages', json = message)

print(messages, file=sys.stderr)
send_message(currentIP, args.message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
