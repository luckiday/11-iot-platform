import os
import jwt
import datetime
from flask import Flask
from flask import request

last_message = ''
def create_app():

    flask_app = Flask(__name__)
    flask_app.config.from_pyfile('config.py')

    ###JWT(flask_app, authenticate, identity)  # /auth

    @flask_app.route('/')
    def index():
        return 'Test: Server running!'

    @flask_app.route('/message',methods = ['POST', 'GET'])
    def message():
        global last_message
        if request.method == 'POST':
            try:
                jwt.decode(request.json['token'], flask_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
            except Exception as e:
                return 'Failed! bad or missing token'
            else: 
                last_message =  jwt.decode(request.json['token'], flask_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])['message']
                return 'Success!'
        else:
            jwt_payload = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=15), 'message':last_message}, flask_app.config['JWT_SECRET_KEY']).decode('utf-8')
            return jwt_payload
    return flask_app


app = create_app()


if __name__ == "__main__":
    app.run()
