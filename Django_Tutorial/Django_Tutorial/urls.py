"""
Definition of urls for Django_Tutorial.
"""

from django.conf.urls import include, url
#from django.urls import path, re_path
from HelloDjangoApp import views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.index, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^algorithms$', views.algorithms, name='algorithms'),
    url(r'^upload$', views.upload, name='upload'),
    
    ]

