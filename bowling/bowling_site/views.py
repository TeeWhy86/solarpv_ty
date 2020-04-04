from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('This is the Index Page...')


def bowling_site_home(request):

    # render function takes argument - request
    # and return HTML as response
    return render(request, "BowlersBliss.html")


def bowling_site_about(request):

    # render function takes argument - request
    # and return HTML as response
    return render(request, "About.html")


def bowling_site_reg(request):

    # render function takes argument - request
    # and return HTML as response
    return render(request, "BowlersBlissRegistration.html")


def bowling_site_contact(request):

    # render function takes argument - request
    # and return HTML as response
    return render(request, "Contact.html")


def bowling_site_log(request):

    # render function takes argument - request
    # and return HTML as response
    return render(request, "Login.html")


def bowling_site_wip(request):

    # render function takes argument - request
    # and return HTML as response
    return render(request, "WIP.html")
