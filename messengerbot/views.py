from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
import os, json
from messengerbot import receive

from TokenManager import TokenManager
tm = TokenManager()
VERIFY_TOKEN = tm.get('MESSENGER_VERIFY_TOKEN')

def index(request):
    return HttpResponse('Front page of ECEUSC Messenger Bot should go here! Heroku 2....')

@csrf_exempt
def webhook(request):
    if request.method == 'GET':
        verify_token = request.GET.get('hub.verify_token')
        
        if verify_token == VERIFY_TOKEN:
            hub_challenge = request.GET.get('hub.challenge')
            print(hub_challenge)
            return HttpResponse(hub_challenge)
        else:
            return HttpResponse('ERROR')
            
    elif request.method == 'POST':
        data = json.loads(request.body.decode("utf-8") )
        
        obj = data.get('object')
        if obj == 'page':
            for entry in data.get('entry'):
                for msg_event in entry.get('messaging'):
                    receive.handleMessage(msg_event)
        else:
            return HttpResponse('this is weird...')
    return HttpResponse(status=200)

