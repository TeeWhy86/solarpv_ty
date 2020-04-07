from django import forms
from .models import Client
# from .models import User


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client

        fields = [
            'clientName',
            'clientType',
        ]
#
#
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'password',
#             'first',
#             'middle',
#             'last',
#             'job',
#             'email',
#             'office',
#             'cell',
#             'prefix',
#             'staff',
#         ]
#
#
# class RawUserForm(forms.Form):
#
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     first = forms.CharField()
#     middle = forms.CharField(required=False)
#     last = forms.CharField()
#     job = forms.CharField()
#     email = forms.EmailField()
#     office = forms.CharField()
#     cell = forms.CharField()
#     prefix = forms.CharField(required=False)
#     staff = forms.CharField()

