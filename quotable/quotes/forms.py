from django import forms
from quotes.models import Quote
from account.models import QuotableUserProfile
from django.contrib.auth.models import User

class QuoteCreationForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)
    sayer = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(QuoteCreationForm, self).__init__(*args, **kwargs)
        self.user = kwargs.pop('user', None)

    def save(self):
        data = self.cleaned_data
        quote = Quote(body=data['body'], sayer=data['sayer'], user=self.user)
        quote.save()

    def clean(self):
        return self.cleaned_data


