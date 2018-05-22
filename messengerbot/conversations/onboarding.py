from ..Messenger import TextMessage, SenderAction, SenderActionMessage, QuickReply, QR_ContentType
from ..send import send_message, get_profile
from enum import Enum
from time import sleep
import re

class PAYLOADS(Enum):
    SUB_EVENTS = 'subscribe_events'

def step1(user, msg_event):
    profile = get_profile(user.psid)

    texts = [
    ( ('Hello %s! I\'m the bot for the ECE Undergrad Student Council' % profile['first_name']) + 
    ', it\'s nice to meet you! '),
    ( 'I\'m here to give you any academic, social, or professional support as an ECE student'),
    ('First up, would you like to recieve any of these notifications from me? ' + 
        'You\'ll be able to choose the frequency next!')
    ]
    notif_qrs = [
        QuickReply(title='Subscribe to ECE Events', payload=PAYLOADS.SUB_EVENTS.value),
    ]
    tms = list(map(lambda x: TextMessage(text=x, psid=user.psid), texts))
    tms[-1].add_quick_reply(notif_qrs)

    for tm in tms:
        send_message(tm)
        sleep(.75)
    user.convo_step_index = 1
    user.save()
    return True

def step2(user, msg_event):
    qr = msg_event.get('message').get('quick_reply')
    if qr is not None:
        if qr.get('payload') == PAYLOADS.SUB_EVENTS.value:
            user.convo_step_index = 2
            user.save()
            ask_for_email(user, msg_event)
            return True
    text = 'I\'m sorry, please select the payload below!'
    tm = TextMessage(psid=user.psid, text=text)
    tm.add_quick_reply(QuickReply(title='Subscribe to ECE Events', payload=PAYLOADS.SUB_EVENTS.value))
    send_message(tm)

    return True

def ask_for_email(user, msg_event):
    texts = [
        ('Thank you for that!'),
        ('Next up, what\'s your @ucsd.edu email address? \n' + 
            'I\'ll use this just to authenticate you as a UCSD student!'),
        ('Feel free to type it out or press on the button below if it matches! ')
    ]
    tms = list(map(lambda x: TextMessage(psid=user.psid, text=x), texts))
    
    tms[-1].add_quick_reply( QuickReply(content_type=QR_ContentType.EMAIL))
    
    for tm in tms:
        send_message(tm)
        sleep(1)

r_ucsd_email = re.compile(r'(^[a-zA-Z0-9_.+-]+@ucsd\.edu$)')

def step3(user, msg_event):
    profile = get_profile(user.psid)
    msg = msg_event.get('message')
    email = msg.get('text') or (msg.get('quick_reply') and msg.get('quick_reply').get('payload'))
    if email is None:
        text = 'Sorry, didn\'t catch that! Please send me your @ucsd.edu email!'
        tm = TextMessage(psid=user.psid, text=text)
        tm.add_quick_reply( QuickReply(content_type=QR_ContentType.EMAIL))
        send_message(tm)
        return
    is_ucsd = r_ucsd_email.search(email)

    if is_ucsd is None:
        text = 'Sorry, please provide a @ucsd.edu email account!'
        tm = TextMessage(psid=user.psid, text=text)
        tm.add_quick_reply( QuickReply(content_type=QR_ContentType.EMAIL))
        send_message(tm)
        return
    
    text = 'Sweet! I\'m going to send you a confirmation email to %s, one sec...' % (email)
    send_message(TextMessage(psid=user.psid, text=text))
    
    res = send_confirmation_email(msg_event['orig_host_name'], user, profile, email)
    if res is True:
        text = 'Email was sent to %s! Please open it and click on the provided link!' % (email)
        send_message(TextMessage(psid=user.psid, text=text))
        user.convo_id = None
        user.convo_step_index = None
        user.save()

    return True

from django.core.mail import send_mail
import uuid

def send_confirmation_email(host, user, profile, email):

    confirm_email_code = str(uuid.uuid4())
    user.email_confirm_code = confirm_email_code
    user.email_is_confirmed = False
    user.ucsd_email = email
    user.save()

    url = host + '/messengerbot/confirm-email?code=%s' % confirm_email_code

    subj = 'ECE USC Messenger Bot - Confirm your email, %s!' % profile.get('first_name')
    body = (
                ('Hey %s! \n\n' % profile.get('first_name')) + 
                'This is the ECE USC Messenger Bot, asking you to please confirm ' + 
                'this email address!\n\n' + 
                'Just click on this link below and you should be good to go: \n\n' +
                ('%s\n\n' % (url)) + 
                'Thank you,\n\n-ECE USC'
            )
    print(subj, body, email)
    try:
        send_mail(subj,body,'eceusc@eng.ucsd.edu' ,[email],fail_silently=False,)
        return True
    except Exception as e:
        print('email was not sent :(',e)
        return False
        



handlers = [step1, step2, step3]
