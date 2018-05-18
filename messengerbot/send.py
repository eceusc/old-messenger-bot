import requests
import json

from TokenManager import TokenManager
tm = TokenManager()

BASE_URL = 'https://graph.facebook.com/v2.6/me/messages'

def send_message(msg):
    headers = {
        'Content-Type':'application/json'
    }
    params = {
        'access_token': tm.get('MESSENGER_ACCESS_TOKEN')
    }
    response = requests.post(BASE_URL, headers=headers, data=str(msg), params=params)
    print(response, response.url,response.text)

