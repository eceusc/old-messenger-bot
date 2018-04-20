import requests
def process(words):
    r = requests.get('https://dog.ceo/api/breeds/image/random').json()
    return {
            "response_type":"ephermal",
            "text":"here you go",
            "attachments": [
                {
                    "image_url": r.get('message'),
                },
             ]
        }
