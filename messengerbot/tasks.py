# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from . import sync_tasks 

@shared_task
def sendConfirmedEmailMessage(psid=None, email=None):
    sync_tasks.sendConfirmedEmailMessage(psid=psid, email=email)

@shared_task
def handleMessageEvent(msg_event):
    sync_tasks.handleMessageEvent(msg_event)
    return
