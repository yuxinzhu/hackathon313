from django.db import models
from django.contrib.auth.models import User
from django_facebook.models import FacebookProfileModel

class QuotableUserProfile(FacebookProfileModel):
    user = models.OneToOneField(User)
