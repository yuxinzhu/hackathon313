from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, redirect
from django.db import IntegrityError
from django.template import RequestContext
from django_facebook.api import FacebookUserConverter, get_persistent_graph
from django.utils.simplejson import loads, dumps
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import password_change
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect

def is_post(request):
    return request.method == "POST"

def is_get(request):
    return request.method == "GET"

def index(request):
	pass

def add_quote(request):
	pass

def delete_quote(request):
	pass

def login_user(request):
    try:
        if request.user.is_authenticated():
            return Http404
        if is_post(request):
        	return Http404
        else:
            return render_to_response("login.html", context_instance = RequestContext(request))
    except Exception as e:
        print e
        return render_to_response("login.html", context_instance = RequestContext(request))
