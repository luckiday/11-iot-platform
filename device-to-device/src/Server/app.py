#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)
# id, time, message
messages = []

@app.route('/todo/api/v1.0/messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages})


@app.route('/todo/api/v1.0/messages/<int:message_id>', methods=['GET'])
def get_message(message_id):
    message = [message for message in messages if message['id'] == message_id]
    if len(message) == 0:
        abort(404)
    return jsonify({'message': message[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/todo/api/v1.0/messages', methods=['POST'])
def create_message():
    if not request.json or not 'title' in request.json:
        abort(400)
    message = {
        'id': messages[-1]['id'] + 1,
        'message': request.json['message'],
        'done': False
    }
    messages.append(message)
    return jsonify({'message': task}), 201

@app.route('/todo/api/v1.0/messages/<int:message_id>', methods=['PUT'])
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
    task[0]['message'] = request.json.get('message', task[0]['message'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = [message for message in messages if message['id'] == message_id]
    if len(message) == 0:
        abort(404)
    messages.remove(message[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
