# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import User


def index(request):
    return HttpResponse('This is the Index Page...')


def solarpvsite_home(request):
    return render(request, 'SolarPV.html')


def solarpvsite_login(request):
    return render(request, 'SolarPVLogin.html')


def solarpvsite_reg(request):
    return render(request, 'SolarPVRegister.html')


def solarpvsite_wp(request):
    return render(request, 'SolarPVWebPortal.html')


def solarpvsite_wip(request):
    return render(request, 'WIP.html')


# def user_detail_view(request):
#     obj = User.objects.get(id=1)
#     context = {
#         'first': obj.first,
#     }
#     return render(request, "user/detail.html", context)
