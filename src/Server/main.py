import os
from flask import Flask, Blueprint
from flask_restful import Api
from flask_jwt import JWT
from flask import request

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
            last_message = request.json['message']
            return 'Post route!'
        else:
            return 'Get route!'

    return flask_app


app = create_app()


if __name__ == "__main__":
    app.run()
