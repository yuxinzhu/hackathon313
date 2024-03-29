from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quotable.views.home', name='home'),
    # url(r'^quotable/', include('quotable.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'account.views.login_user'),
    url(r'^$', 'account.views.login_user'),
    url(r'^create/$', 'quotes.views.create'),
    url(r'^newsfeed/$', 'quotes.views.newsfeed'),
    url(r'^me/$', 'account.views.me'),
    url(r'^logout/$', 'account.views.logout_user'),
    (r'^facebook/', include('django_facebook.urls')),
)
