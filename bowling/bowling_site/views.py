from django.shortcuts import render

# Create your views here.


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


def bowling_site_login(request):

    # render function takes argument - request
    # and return HTML as response
    return render(request, "Login.html")


def bowling_site_wip(request):

    # render function takes argument - request
    # and return HTML as response
    return render(request, "WIP.html")
