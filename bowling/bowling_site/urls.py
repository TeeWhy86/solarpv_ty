# from django.contrib import admin
from django.urls import path

# importing views from views..py
from .views import *

urlpatterns = [
    path('', index),
    path('home', bowling_site_home),
    path('about', bowling_site_about),
    path('reg', bowling_site_reg),
    path('contact', bowling_site_contact),
    path('log', bowling_site_log),
    path('wip', bowling_site_wip),
]
