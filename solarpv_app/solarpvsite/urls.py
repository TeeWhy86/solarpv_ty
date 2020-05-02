from django.urls import path

from . import views
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    path('', solarpvsite_home, name='home'),
    path('log', solarpvsite_login, name='login'),
    path('reg', user_form, name='registration'),
    path('wp', solarpvsite_wp, name='web portal'),
    path('wip', solarpvsite_wip, name='under construction'),
    path('create/', create_client),
    path('retrieve/', list_client),
    path('detail/<id>', detail_client),
    path('update/<id>', update_client),
    path('delete/<id>', delete_client),
    path('search/', SearchCertView.as_view(), name='search_results'),
    path('cert_search/', CertSearch.as_view(), name='cert_search')
]
