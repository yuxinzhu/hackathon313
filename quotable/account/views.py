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
from django_facebook.api import FacebookUserConverter, get_persistent_graph, get_facebook_graph
from account.utils import is_get, is_post

@login_required
def retrieve_friends(request, field='uid'):
    try:
        open_graph = get_persistent_graph(request)
        converter = FacebookUserConverter(open_graph)
        friends = converter.get_friends()
        friends_data = [u[field] for u in friends]
        return friends_data
    except Exception as e:
        return []
        print e

@login_required
def me(request):
    quotes = Quotable.objects.all(user=request.user.getProfile())
    render_to_response("me.html", {'quotes': quotes}, context_instance = RequestContext(request))

# @login_required
# def retrieve_friend_quotes(request, friend_id):
#     quotes = Quoteable.objects.all(sayer=friend_id)
#     render_to_response("person.html", context_instance = RequestContext(request))

# @login_required
# def retrieve_all_quotes(request):
#     quotes = Quoteable.objects.filter(user__facebook_id__in=retrieve_friends(request, field='uid')).order_by('date_created')
#     render_to_response("person.html", context_instance = RequestContext(request))

def logout_user(request):
    if is_post(request):
        logout(request)
        return redirect("/")
    return redirect("/")

def login_user(request):
    try:
        if request.user.is_authenticated():
            # retrieve_friends(request)
            return render_to_response("newsfeed.html", context_instance = RequestContext(request))
        else:
            return render_to_response("login.html", context_instance = RequestContext(request))
    except Exception as e:
        print e
        return render_to_response("login.html", context_instance = RequestContext(request))
