from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Client
from .forms import ClientForm


# from .forms import UserForm, RawUserForm
# from .models import User

# Create your views here.


def create_client(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form = ClientForm()

    context = {
        'form': form
    }

    # context[form] = form
    return render(request, "backend/create_client.html", context)


def list_client(request):
    context = {}
    context["dataset"] = Client.objects.all()
    return render(request, "backend/list_client.html", context)


def detail_client(request, id):
    context = {}
    context["data"] = Client.objects.get(id = id)
    return render(request, "backend/detail_client.html", context)


def update_client(request, id):
    context = {}
    obj = get_object_or_404(Client, id=id)
    form = ClientForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect("/"+id)

    context["form"] = form
    return render(request, "backend/update_client.html", context)


def delete_client(request, id):
    context = {}
    obj = get_object_or_404(Client, id = id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "backend/delete_client.html", context)

# def user_create_view(request):
#     form = UserForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = UserForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, "backend/user_create.html", context)


# def user_create_view(request):
#     my_form = RawUserForm()
#     if request.method == "POST":
#         my_form = RawUserForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             User.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         'form': my_form
#     }
#     return render(request, "backend/user_create.html", context)


# def user_create_view(request):
#
#     context = {}
#     return render(request, "backend/user_create.html", context)
