from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import django_filters
from .models import Product

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class ProductFilter(django_filters.FilterSet):
    
    price = django_filters.AllValuesFilter()

    class Meta:
        model = Product
        fields = ['price']