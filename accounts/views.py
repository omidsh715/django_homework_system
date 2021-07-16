from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
# Create your views here.


class Login(LoginView):
    success_url = 'core:success'
    # authentication_form =


class Signup(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = "signup_form.html"
