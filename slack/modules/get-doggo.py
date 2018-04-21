import requests

def process(words):
    l = 'https://random.dog/woof.json'
    r = requests.get(l).json()
    return {
            "response_type":"ephermal",
            "text":"good dogs are good",
            "attachments": [
                {
                    "image_url": r.get('url'),
                },
             ]
        }
