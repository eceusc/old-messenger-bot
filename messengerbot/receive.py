from . import send 
from .models import User

def handleMessage(msg_event):
    if msg_event.get('message'):
        handle_text(msg_event)
    elif msg_event.get('postback'):
        handle_postback(msg_event)
    elif msg_event.get('referral'):
        handle_referral(msg_event)

def handle_text(msg_event):
    sender = msg_event.get('sender').get('id')
    try:
        u = User.objects.get(psid=sender)
    except Exception as e:
        print('got exception ', e)
        u = User(psid=sender)
        u.save()
    print('after all that', u)
    send.send_message({
      "messaging_type": "RESPONSE",
      "recipient": {
        "id": msg_event.get('sender').get('id')
      },
      "message": {
        "text": msg_event.get('message').get('text')[::-1].upper()      }
    })
    return
def handle_postback(msg_event):
    
    return
def handle_referral(msg_event):
    
    return
