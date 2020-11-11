import os
import requests
import time
import jwt
import datetime
from os.path import join, dirname
from dotenv import load_dotenv

def contact_base():
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY')
    #url = 'http://127.0.0.1:8000'
    url = 'http://cs211-server.herokuapp.com'
    counter = 1
    while(True):
        headers = {'Content-Type': 'application/json',}
        jwt_payload = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=15), 'message':counter}, JWT_SECRET_KEY).decode('utf-8')
        data = '{"token":"' + str(jwt_payload) + '"}'
        response = requests.post(url + '/message', headers=headers, data=data)
        print(response.text)
        r = requests.get(url + '/message')
        try:
            jwt.decode(r.text, JWT_SECRET_KEY, algorithms=['HS256'])
        except:
            print('Failed Server down')
        else: 
            print(jwt.decode(r.text, JWT_SECRET_KEY, algorithms=['HS256'])['message'])
        counter+=1
        time.sleep(10)



if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    contact_base()
