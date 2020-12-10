import requests
import argparse
import sys
import simplejson as json
import base64
import socket

from flask import Flask, jsonify, abort, make_response, redirect, request, render_template

app = Flask(__name__)

serverIP = '192.168.10.20:8000'
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
currentIP = '{}:5000'.format(local_ip)

parser = argparse.ArgumentParser()

parser.add_argument('--deviceID', help='Please select a device from the list')
parser.add_argument('--message', help='Please send a message to device')

args = parser.parse_args()

available_devices = []
messages = []
failed_messages = []
deviceID = 1


def get_devices():
    deviceRequest = requests.get('http://' + serverIP + '/api/devices')
    return deviceRequest.json()

def ping_server():
    global available_devices
    deviceRequest = requests.get('http://' + serverIP + '/api/devices/' + currentIP)
    if 'device' in deviceRequest.json():
        print('Device in Server', file=sys.stderr)
    else:
        device = {'ip' : currentIP}
        deviceRequest = requests.post('http://' + serverIP + '/api/devices', json = device)
    available_devices = get_devices()['devices']

@app.route('/')
def home():
    global deviceID
    ping_server()
    for device in available_devices:
        if device['ip'] == currentIP:
            deviceID = device['device_id']
    return render_template('index.html', available_devices = available_devices, messages=messages, currentDevice = deviceID)

@app.route('/submit', methods=['POST'])
def submit():
    message = request.form.get('message')
    option = request.form.get('devices')
    json_option = json.loads(option.replace("'", "\""))
    message_bytes = message.encode('ascii')
    send_message(json_option['ip'], base64.b64encode(message_bytes))
    return redirect('/')


@app.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages})

@app.route('/api/messages', methods=['POST'])
def create_message():
    if not request.json:
        abort(400)

    decoded_message = base64.b64decode(request.json['message']).decode('ascii')
    message = {
        'device_id': deviceID,
        'origin_device': request.json['origin_device'],
        'id': request.json['id'],
        'message': decoded_message,
        'done': False
    }
    messages.append(message)
    return jsonify({'message': message}), 201

def send_message(target_ip, message):
    ping_server()
    device = [device for device in available_devices if device['ip'] == target_ip]
    if not device:
        print('Target Device does not exist', file=sys.stderr)
        return
    json_message = {'target_device' : device[0], 'device_id': deviceID, 'message': message}
    messageRequest = requests.post('http://' + serverIP + '/api/messages', json = json_message)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
