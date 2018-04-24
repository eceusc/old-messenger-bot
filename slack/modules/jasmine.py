#jasmine.py
def process(words):
    import datetime
    msg = 'Right now it is: ' +str(datetime.datetime.now()) + 'and Jasmine LOVES Costco'
    if words==[]:
        return msg 
    if words[0]=='Hello':
        return 'Hey to you too!'

