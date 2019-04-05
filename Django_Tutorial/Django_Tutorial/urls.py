"""
Definition of urls for Django_Tutorial.
"""

from django.conf.urls import include, url
import HelloDjangoApp.views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    
    url(r'^$', HelloDjangoApp.views.index, name='index'),
    url(r'^home$', HelloDjangoApp.views.home, name='home'),
    url(r'^time$', HelloDjangoApp.views.time, name='time'),
    url(r'^time_template$', HelloDjangoApp.views.time_template, name='time_template'),

    ]
