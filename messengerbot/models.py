from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    psid = models.CharField(max_length=30, unique=True)
    ucsd_email = models.CharField(max_length=50, null=True)
    email_is_confirmed = models.NullBooleanField(null=True)
    email_confirm_code = models.UUIDField(default=uuid.uuid4)

    convo_id = models.PositiveSmallIntegerField(null=True)
    convo_step_index = models.PositiveSmallIntegerField(null=True)
    subscribe_events = models.NullBooleanField(null=True)
    
    def __str__(self):
        email = self.ucsd_email or '  '
        return '{{ {} | {} | {}...@ucsd.edu}}'.format(self.id, self.psid, self.ucsd_email[:2])
    def is_in_convo(self):
        print((type(self.convo_id), self.convo_id))
        return self.convo_id is not None and self.convo_id >= 0
