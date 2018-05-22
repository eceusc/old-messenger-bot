import requests
import json

from TokenManager import TokenManager
tm = TokenManager()

BASE_URL = 'https://graph.facebook.com/v2.6/me/messages'

def get_profile(psid):
    headers = {
        'Content-Type':'application/json'
    }
    params = (
        ('access_token=%s' % tm.get('MESSENGER_ACCESS_TOKEN')) + 
        '&fields=first_name,last_name,profile_pic,locale,timezone,gender'
    )
    PROFILE_URL = 'https://graph.facebook.com/v2.6/%s' % str(psid)
    response = requests.get(PROFILE_URL, headers=headers, params=params)
    return response.json()

def send_message(msg):
    headers = {
        'Content-Type':'application/json'
    }
    params = {
        'access_token': tm.get('MESSENGER_ACCESS_TOKEN')
    }
    response = requests.post(BASE_URL, headers=headers, data=str(msg), params=params)

