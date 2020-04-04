from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('home', solarpvsite_home),
    path('login', solarpvsite_login),
    path('reg', solarpvsite_reg),
    path('wp', solarpvsite_wp),
    path('wip', solarpvsite_wip),
]