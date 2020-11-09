import os
import postgresql
import datetime
import postgresql.driver as pg_driver
from flask import Flask, Blueprint
from flask_restful import Api
from flask_jwt import JWT
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
        if request.method == 'POST':
            global last_message
            last_message = request.json['message']
            return 'Success!'
        else:
            global last_message
            return last_message

    return flask_app


app = create_app()


if __name__ == "__main__":
    app.run()
