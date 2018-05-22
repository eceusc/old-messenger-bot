
from .models import User
from .Messenger import TextMessage, SenderAction, SenderActionMessage, QuickReply
from .send import send_message
from .conversation_handler import handleConversation

from time import sleep
import datetime

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def sendConfirmedEmailMessage(psid=None, email=None):
    text = 'Just confirmed your email (%s), thank you so much!' % email
    send_message(TextMessage(psid=psid, text=text))
    return True

def handleMessageEvent(msg_event):
    sender = msg_event.get('sender').get('id')
    msg = msg_event.get('message')

    try:
        u = User.objects.get(psid=sender)
    except User.DoesNotExist:
        u = User(psid=sender)
        u.save()

    if u.is_in_convo():
        print('inside comvo')
        print(u.convo_id)
        handleConversation(u, msg_event)
        return

    if 'put me in ' in msg.get('text'):
        print('inside put me in')
        convo_id = int(msg.get('text')[len('put me in '):])
        u.convo_id = convo_id
        u.convo_step_index = 0
        u.save()
        print('put me in, convo_id=%d, u.convo_id=%d' % (convo_id, u.convo_id))
        handleConversation(u, msg_event)
        return

    send_message(TextMessage(text=('got message at |%s' % ((datetime.datetime.now()))), psid=sender))
    #send_message(SenderActionMessage(psid=sender, sender_action=SenderAction.MARK_SEEN))
    #sleep(.5)
    #send_message(SenderActionMessage(psid=sender, sender_action=SenderAction.TYPING_ON))

    #sleep(8)
    msg = str(u) + '& ' + msg_event.get('message').get('text')[::-1].upper()
    last_msg = TextMessage(text=msg, psid=sender)
    last_msg.add_quick_reply( QuickReply( title='title', payload='payload'  ))
    #send_message(SenderActionMessage(psid=sender, sender_action=SenderAction.TYPING_OFF))
    send_message(last_msg)

    return
