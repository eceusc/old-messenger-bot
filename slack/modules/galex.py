class SlackMessage():
    def __init__(self, text, username, mrkdwn, attachments):
        return
help = '[council member name]'
def process(words):
    if len(words) > 1:
        resp = {
            "response_type":"ephermal",
            "text":"here you go",
            "attachments": [
                {
                    "image_url": 'http://eceusc.ucsd.edu/pics/17-18/' + words[1]  +  '.jpg',
                },
             ]
        }
        return resp
    else:
        return 'oh :('
