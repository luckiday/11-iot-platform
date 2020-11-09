import os
import requests
import time

def contact_base():
    counter = 1
    while(True):
        headers = {'Content-Type': 'application/json',}
        data = '{"message":"' + str(counter) + '"}'
        response = requests.post('http://cs211-server.herokuapp.com/message', headers=headers, data=data)
        print(response.text)
        r = requests.get('https://cs211-server.herokuapp.com/message')
        print(r.text)
        counter+=1
        time.sleep(10)



if __name__ == "__main__":
    contact_base()
