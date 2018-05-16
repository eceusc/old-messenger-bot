import json
import os

ENV_TOKEN_KEYS = [
    'MESSENGER_VERIFY_TOKEN', 
    'MESSENGER_ACCESS_TOKEN', 
    'SLACK_TOKEN',
]

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class TokenManager():

    def __init__(self):

        self.tokens = {}
        
        # Add env vars first
        for key in ENV_TOKEN_KEYS:
            self.tokens[key] = os.environ.get(key)

        # See if config.json has everythin
        # None: config.json tokens will replace env var token if same name
        try:
            tokens = json.load(open('config.json')).get('tokens')
            for tok_key in tokens:
                self.tokens[tok_key] = tokens.get(tok_key)
        except Exception as e:
            print(e)
            print('No config.json available, continuing...')

        return
    
    def get(self, key=None):
        if key:
            token = self.tokens.get(key)
            return token
        else:
            return None
