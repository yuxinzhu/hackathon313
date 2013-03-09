from django.db import models

class Quote(models.Model):
    user = models.ForeignKey('account.QuotableUserProfile')
    body = models.TextField()
    sayer = models.CharField(max_length=100)
    date_created = models.DatetimeField(auto_now=True)

class Tag(models.Model):
	text = models.CharField(max_length=100)


