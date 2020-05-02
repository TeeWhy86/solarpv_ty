# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .forms import *


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


# FORM VIEWS

def client_form(request):
    form = ClientForm()
    if form.is_valid():
        form.save()
        form = ClientForm()

    context = {
        'form': form
    }
    return render(request, "SolarPVWebPortal.html", context)


def user_form(request):
    form = UserForm()
    if form.is_valid():
        form.save()
        form = UserForm()

    context = {
        'form': form
    }
    return render(request, "SolarPVRegister.html", context)


def create_client(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form = ClientForm()

    context = {
        'form': form
    }

    # context[form] = form
    return render(request, "create_client.html", context)


def list_client(request):
    context = {}
    context["dataset"] = Client.objects.all()
    return render(request, "list_client.html", context)


def detail_client(request, id):
    context = {}
    context["data"] = Client.objects.get(id = id)
    return render(request, "detail_client.html", context)


def update_client(request, id):
    context = {}
    obj = get_object_or_404(Client, id=id)
    form = ClientForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect("/"+id)

    context["form"] = form
    return render(request, "update_client.html", context)


def delete_client(request, id):
    context = {}
    obj = get_object_or_404(Client, id = id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "delete_client.html", context)


class CertSearch(TemplateView):
    template_name = 'Cert_Search.html'


class SearchCertView(ListView):
    model = Client
    template_name = 'search_cert.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Client.objects.filter(
            Q(clientName__icontains=query) | Q(clientType__icontains=query)
        )
        return object_list
