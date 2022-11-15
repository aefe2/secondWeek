from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from project.forms import RegisterUserForm


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


class RegisterView(CreateView):
    template_name = 'registration/signup.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
