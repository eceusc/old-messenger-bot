from enum import Enum
import json

def main():
    msg = TextMessage('lol', 1231232)
    print(msg.serialize())

    msg = ImageMessage('this is the url', psid=1231232)
    print(msg.serialize())

class SenderAction(Enum):
    MARK_SEEN = 'mark_seen'
    TYPING_OFF = 'typing_off'
    TYPING_ON = 'typing_on'

class MessagingType(Enum):
    RESPONSE = 'RESPONSE'

class SenderActionMessage():
    def __init__(self, recipient={}, sender_action=SenderAction.MARK_SEEN, **kwargs):
        self.recipient = recipient
        self.sender_action = sender_action

        if kwargs.get('psid') is not None:
            self.recipient = { 'id': kwargs.get('psid')}
        if kwargs.get('phone_number') is not None:
            self.recipient = { 'phone_number': kwargs.get('phone_number')}
        return

    def __str__(self):
        s = self.serialize()
        print(s)
        print('asdffdsa')
        print(json.dumps(s))
        return json.dumps(self.serialize())

    def serialize(self):
        return {
            'recipient':self.recipient,
            'sender_action':self.sender_action.value
        }
class Message():
    def __init__( self, 
                messaging_type=MessagingType.RESPONSE,
                recipient={}, 
                message={},
                **kwargs
    ):

        self.messaging_type = messaging_type #, 'UPDATE', '<MESSAGE_TAG>'
        self.recipient = recipient # id, phone_number, plugin stufff
        self.message = message

        if kwargs.get('psid') is not None:
            self.recipient = { 'id': kwargs.get('psid')}
        if kwargs.get('phone_number') is not None:
            self.recipient = { 'phone_number': kwargs.get('phone_number')}

        return

    def send(self):
        return
    def __str__(self):
        return json.dumps(self.serialize())

    def serialize(self):
        return {
            'messaging_type':self.messaging_type.value,
            'recipient':self.recipient,
            'message':self.message
        }

class TextMessage(Message):
    def __init__(self, text='', psid=None, **kwargs):
        super().__init__(psid=psid, **kwargs)
        #if len(text) == 0:
        self.message = {
            'text':text
            }
        return

class AttachmentMessage(Message):
    def __init__(self, attachment_type=None, payload=None, psid=None, **kwargs):
        super().__init__(psid=psid, **kwargs)

        # TODO check type 
        self.message = {
                'type': attachment_type,
                'payload': payload
        }

        return
class ImageMessage(AttachmentMessage):
    def __init__(self, url, psid, **kwargs):
        payload = {
            'url':url,
            'is_reusable':True
            }
        super().__init__(attachment_type='image', payload=payload, **kwargs)

if __name__ == '__main__':
    main()
