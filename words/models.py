from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.

class Word(models.Model):
    word = models.TextField(blank=True, null=True)
    meaning = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    