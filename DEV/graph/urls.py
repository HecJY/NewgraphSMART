from django.urls import path
from django.conf.urls import url, re_path

from . import views

app_name = 'graph'
urlpatterns = [
    path('viewgraph/', views.viewgraph, name='viewgraph')
    ]
