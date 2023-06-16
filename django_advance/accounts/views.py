from django.shortcuts import render

# Create your views here.

from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AccountCreateView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "accounts/accounts_create.html"
    success_url = reverse_lazy('accounts:create')