import requests
def process(words):
    l = 'https://random.dog/woof.json'
    r = requests.get(l).json()
    return {
            "response_type":"ephermal",
            "text":"here you go",
            "attachments": [
                {
                    "image_url": r.get('url'),
                },
             ]
        }
