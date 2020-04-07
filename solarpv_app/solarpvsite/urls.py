from django.urls import path

from . import views
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    path('', solarpvsite_home, name='home'),
    path('login', solarpvsite_login, name='login'),
    path('reg', solarpvsite_reg, name='registration'),
    path('wp', solarpvsite_wp, name='web portal'),
    path('wip', solarpvsite_wip, name='under construction'),
]