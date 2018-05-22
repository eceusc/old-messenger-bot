import json
import os

ENV_TOKEN_KEYS = [
    'MESSENGER_VERIFY_TOKEN', 
    'MESSENGER_ACCESS_TOKEN', 
    'DJANGO_TOKEN',
    'SLACK_TOKEN',
    'DATABASE_URL',
    'REDIS_URL',
    'EMAIL_HOST',
    'EMAIL_HOST_PASSWORD',
    'EMAIL_HOST_USER',
    'EMAIL_PORT'
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
            env_token = os.environ.get(key)
            if env_token is not None and len(env_token) > 0:
                self.tokens[key] = env_token

        # See if config.json has anything
        # None: config.json tokens will replace env var token if same name
        try:
            tokens = json.load(open('config.json')).get('tokens')
            for tok_key in tokens:
                file_token = tokens.get(tok_key)
                if file_token is not None and len(file_token) > 0:
                    self.tokens[tok_key] = file_token
        except Exception as e:
            print(e, 'No config.json available, continuing...')
        
        return
    
    def get(self, key=None):
        if key:
            token = self.tokens.get(key)
            return token
        else:
            return None
