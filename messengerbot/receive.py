from . import send 

def handleMessage(msg_event):
    if msg_event.get('message'):
        handle_text(msg_event)
    elif msg_event.get('postback'):
        handle_postback(msg_event)
    elif msg_event.get('referral'):
        handle_referral(msg_event)

def handle_text(msg_event):
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
