import requests

from TokenManager import TokenManager
tm = TokenManager()

BASE_URL = 'https://graph.facebook.com/v2.6/me/messages'

def send_message(msg):
    headers = {
        'Content-Type':'application/json'
    }
    params = {
        access_token:tm.get('MESSENGER_ACCESS_TOKEN')
    }
    r = requests.post(BASE_URL, headers=headers, data=msg, params=params)


