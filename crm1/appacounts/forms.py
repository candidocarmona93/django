from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import orders
from .models import custumer


class CustumerForm(ModelForm):
    class Meta:
        model = custumer
        fields = '__all__'
        exclude = ['user']


class ordersForm(ModelForm):
    class Meta:
        model = orders
        fields = '__all__' 


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']