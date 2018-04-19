from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import os, sys
from slack.modules import * 

SLACK_TOKEN = os.environ['SLACK_TOKEN']

def index(request):
    return HttpResponse('Front page of ECEUSC Slack Bot should go here!')

@csrf_exempt
def command(request):

    if request.method == 'GET':
        return HttpResponse('Lol lets do this')

    elif request.method == 'POST':
        req_token = request.POST.get('token')

        if req_token != SLACK_TOKEN:
            return HttpResponse('WRONG TOKEN', status=401)

        user_id = request.POST.get('user_id')
        channel_id = request.POST.get('channel_id')
        channel_name = request.POST.get('channel_name')
        text = request.POST.get('text')
        words = text.split(' ')
        command = words[0]
        response = get_response(command, words)
        return response

class SlackMessage():
    def __init__(self, text, username, mrkdwn, attachments):
        return

def get_response(command, words):
    cmd_response = sys.modules['slack.modules.' + command].process(words)

    if isinstance(cmd_response, str):
        return HttpResponse(cmd_response, status=200)
    elif isinstance(cmd_response, dict):
        return JsonResponse(cmd_response, status=200)
    else:
        try:
            cmd_response = str(cmd_response)
            return HttpResponse(cmd_response, status=200)
        except e:
            return HttpResponse('oh oh :(', status=200)
