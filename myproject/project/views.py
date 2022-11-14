from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')