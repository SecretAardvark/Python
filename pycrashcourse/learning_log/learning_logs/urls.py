from django.conf.urls import url
from . import views
"""defines urls for learning_logs"""
urlpatterns = [

    url(r'^$', views.index, name = 'index')
]