from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from words import models as word_models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete  = models.CASCADE)
    last_visited_word = models.ForeignKey(word_models.Word, default=4760, on_delete = models.CASCADE)

def create_user_profile(sender, instance, created, **kwargs):
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 