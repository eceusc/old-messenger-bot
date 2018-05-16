import requests
import json

from TokenManager import TokenManager
tm = TokenManager()

BASE_URL = 'https://graph.facebook.com/v2.6/me/messages'

def send_message(msg):
    print('inside send_message')
    headers = {
        'Content-Type':'application/json'
    }
    params = {
        'access_token': tm.get('MESSENGER_ACCESS_TOKEN')
    }
    print('aaaa',msg)
    response = requests.post(BASE_URL, headers=headers, data=json.dumps(msg), params=params)
    print(response, response.url,response.text)

