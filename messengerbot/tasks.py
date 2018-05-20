# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger

from .models import User
from .Messenger import TextMessage, SenderAction, SenderActionMessage
from .send import send_message
from time import sleep
import datetime

@shared_task
def handleMessageEvent(msg_event):
    sender = msg_event.get('sender').get('id')
    send_message(TextMessage(text=('got message at |%s' % ((datetime.datetime.now()))), psid=sender))
    #send_message(SenderActionMessage(psid=sender, sender_action=SenderAction.MARK_SEEN))
    #sleep(.5)
    #send_message(SenderActionMessage(psid=sender, sender_action=SenderAction.TYPING_ON))

    try:
        u = User.objects.get(psid=sender)
    except Exception as e: # User.NotFound or something
        u = User(psid=sender)
        u.save()
    sleep(8)
    msg = str(u) + '& ' + msg_event.get('message').get('text')[::-1].upper()
    #send_message(SenderActionMessage(psid=sender, sender_action=SenderAction.TYPING_OFF))
    send_message(TextMessage(text=msg, psid=sender))

    return
