import os
import requests
import time
import jwt
import datetime
import uuid 
from os.path import join, dirname
from dotenv import load_dotenv

def contact_base():
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY')
    if os.environ.get('DEVICE_CODE'):
        DEVICE_CODE_VALUE = os.environ.get('DEVICE_CODE')
    else:
        DEVICE_CODE_VALUE = str(time.time()) + str(hex(uuid.getnode()))
        file_obj = open('.env', 'a')
        file_obj.write('\nDEVICE_CODE=' + str(DEVICE_CODE_VALUE))
        file_obj.close()
    #url = 'http://127.0.0.1:8000'
    url = 'https://cs211-server.herokuapp.com'
    counter = 1
    while(True):
        headers = {'Content-Type': 'application/json',}
        data_packet = str(counter) + str(DEVICE_CODE_VALUE)
        jwt_payload = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=15), 'message':str(data_packet)}, JWT_SECRET_KEY).decode('utf-8')
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
