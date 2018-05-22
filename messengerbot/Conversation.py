
class Conversation():
    def __init__(self, name, convo_id, handlers=[]):
        self.name = name
        self.convo_id = convo_id
        self.handlers = handlers

    def handle(self, handler_index, **kwargs):
        self.handlers[handler_index](**kwargs)
