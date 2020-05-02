from django import forms
from .models import *


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client

        fields = [
            'clientName',
            'clientType',
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first',
            'middle',
            'last',
            'job',
            'email',
            'office',
            'cell',
            'prefix',
            'staff',
        ]
