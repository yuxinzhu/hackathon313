from django.db import models
from django.contrib.auth.models import User
from django_facebook.models import FacebookProfileModel
from django.db.models.signals import post_save

class QuotableUserProfile(FacebookProfileModel):
    user = models.OneToOneField(User)

def create_facebook_profile(sender, instance, created, **kwargs):
    '''
    Make sure a QuotableUserProfile is created when creating a
    user.
    '''
    if created:
        QuotableUserProfile.objects.create(user=instance)

post_save.connect(create_facebook_profile, sender=User)

def user_post_delete(sender, instance, **kwargs):
    try:
        BerekleytimeUserProfile.objects.get(user=instance).delete()
    except:
        pass

def user_post_save(sender, instance, **kwargs):
    try:
        profile, new = QuotableUserProfile.objects.get_or_create(user=instance)
    except:
        pass

models.signals.post_delete.connect(user_post_delete, sender=User)
models.signals.post_save.connect(user_post_save, sender=User)
