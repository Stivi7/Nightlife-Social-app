from django.db import models
from social_django.models import USER_MODEL

# Create your models here.

class CheckIn (models.Model):
    buttonId = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    owner = models.ForeignKey(USER_MODEL)

    def __str__(self):
        return self.buttonId
