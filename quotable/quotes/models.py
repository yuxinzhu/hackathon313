from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_facebook.models import FacebookProfileModel

class Quote(models.Model):
    user = models.ForeignKey('account.QuotableUserProfile')
    body = models.TextField()
    sayer = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now=True)

class Tag(models.Model):
	text = models.CharField(max_length=100)


