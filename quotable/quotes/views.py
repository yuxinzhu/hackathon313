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
        print '2'
        if is_post(request):
            print 'hey1'
            body = str(request.POST["body"])
            sayer = str(request.POST["sayer"])
            if body and sayer and len(sayer) <= 99:
                name_to_uid = retrieve_friends_dict(request)
                print name_to_uid
                sayer = name_to_uid[sayer.upper()] if sayer.upper() in name_to_uid else sayer
                print sayer
                redirect('/newsfeed')
        return render_to_response("create.html", context_instance = RequestContext(request))
    except Exception as e:
        print str(e)

def newsfeed(request):
    return
