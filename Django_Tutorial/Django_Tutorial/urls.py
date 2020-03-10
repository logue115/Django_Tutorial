"""
Definition of urls for Django_Tutorial.
"""

from django.conf.urls import include, url
#from django.urls import path, re_path
import HelloDjangoApp.views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    
    url(r'^$', HelloDjangoApp.views.index, name='index'),
    url(r'^home$', HelloDjangoApp.views.index, name='home'),
    url(r'^about$', HelloDjangoApp.views.about, name='about'),
    url(r'^algorithms$', HelloDjangoApp.views.algorithms, name='algorithms'),
    url(r'^upload$', HelloDjangoApp.views.upload, name='upload'),
    
    ]
