#julius.py
def process(words):
    if words[0] == 'hello' or words[0] == 'Hello':
        return 'Hello'
    elif words[0] == 'goodbye' or words[0] == 'Goodbye':
        return 'Goodbye!'
    else:
        return 'Sorry, I don\'t understand!'   # Message to send back
