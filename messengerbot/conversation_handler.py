from .conversations import onboarding
from .Conversation import Conversation

CONVO_MAP = {
    0: Conversation(name='Onboarding', convo_id=0, handlers=onboarding.handlers),
}

def handleConversation(u, msg_event):
    print(u.convo_id)
    CONVO_MAP[u.convo_id].handle(u.convo_step_index, user=u, msg_event=msg_event)
