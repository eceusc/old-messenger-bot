from django.db import models

# Create your models here.

class User(models.Model):
    psid = models.CharField(max_length=30, unique=True)
    ucsd_email = models.CharField(max_length=50)
    
    def __str__(self):
        email = self.ucsd_email or '  '
        return '{{ {} | {} | {}...@ucsd.edu}}'.format(self.id, self.psid, self.ucsd_email[:2])
