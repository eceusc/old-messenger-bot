from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
import os, json
from messengerbot import receive
try:
    assert 2==3
    from messengerbot.tasks import handleMessageEvent, sendConfirmedEmailMessage
except:
    print('Cant import celery stuff, trying other way...')
    from messengerbot.sync_tasks import handleMessageEvent, sendConfirmedEmailMessage

import datetime
from .models import User

from TokenManager import TokenManager
tm = TokenManager()
VERIFY_TOKEN = tm.get('MESSENGER_VERIFY_TOKEN')

def index(request):
    return HttpResponse('Front page of ECEUSC Messenger Bot should go here! %s' % request.get_host())

#confirm-email?code=%s
def confirm_email(request):
    code = request.GET.get('code')
    try:
        u = User.objects.get(email_confirm_code=code)
    except User.DoesNotExist:
        return HttpResponse('I\'m sorry, I don\'t recognize that code!')
    if u.email_is_confirmed:
        return HttpResponse('Your email has already been confirmed!')
    u.email_is_confirmed = True
    u.save()
    try:
        sendConfirmedEmailMessage.delay(psid=u.psid, email=u.ucsd_email)
    except:
        sendConfirmedEmailMessage(psid=u.psid, email=u.ucsd_email)


    return HttpResponse('Your email has been confirmed! :)')

@csrf_exempt
def webhook(request):
    if request.method == 'GET':
        verify_token = request.GET.get('hub.verify_token')
        
        if verify_token == VERIFY_TOKEN:
            hub_challenge = request.GET.get('hub.challenge')
            return HttpResponse(hub_challenge)
        else:
            return HttpResponse('ERROR')
            
    elif request.method == 'POST':
        data = json.loads(request.body.decode("utf-8") )
        
        obj = data.get('object')
        if obj == 'page':
            for entry in data.get('entry'):
                for msg_event in entry.get('messaging'):
                    #receive.handleMessage(msg_event)
                    msg_event['orig_host_name'] = request.get_host()
                    try:
                        handleMessageEvent.delay(msg_event)
                    except:
                        handleMessageEvent(msg_event)
        else:
            return HttpResponse('this is weird...')
    return HttpResponse(status=200)

