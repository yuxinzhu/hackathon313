from account.utils import is_post, is_get
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, redirect
from django.db import IntegrityError
from django.template import RequestContext
from django.utils.simplejson import loads, dumps
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.views import password_change
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from quotes.models import Quote
from account.utils import retrieve_friends_dict, is_post, is_get
from django_facebook.api import FacebookUserConverter, get_persistent_graph, get_facebook_graph

@login_required
def create(request):
    try:
        if is_post(request):
            body = str(request.POST["body"])
            sayer = str(request.POST["sayer"])
            if body and sayer and len(sayer) <= 99:
                name_to_uid = retrieve_friends_dict(request)
                sayer_id = name_to_uid[sayer.upper()] if sayer.upper() in name_to_uid else sayer
                Quote.objects.create(user=request.user.get_profile(), body=body, sayer=sayer, sayer_id=sayer_id)
                redirect('/newsfeed')
        return render_to_response("create.html", context_instance = RequestContext(request))
    except Exception as e:
        print str(e)

def newsfeed(request):
    quotes = [{'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 'sayer': 'Yuxin Zhu', 'sayer_id': '1234567890'}, {'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 'sayer': 'Yuxin Zhu', 'sayer_id': '1234567890'}, {'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 'sayer': 'Yuxin Zhu', 'sayer_id': '1234567890'}]
    return render_to_response("newsfeed.html", {'quotes': quotes}, context_instance = RequestContext(request))



# class Quote(models.Model):
    # user = models.ForeignKey('account.QuotableUserProfile')
    # body = models.TextField()
    # sayer = models.CharField(max_length=100)
    # sayer_id = models.CharField(max_length=100)
    # date_created = models.DateTimeField(auto_now=True)
