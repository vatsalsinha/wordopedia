from django.db import models

# Create your models here.
class Word(models.Model):
    word = models.TextField(blank=True, null=True)
    meaning = models.TextField(blank=True, null=True)