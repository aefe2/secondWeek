from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Aplication
from project.forms import RegisterUserForm


# Create your views here.

def index(request):
    counter = Aplication.objects.filter(status='received').all().count()
    done = Aplication.objects.filter(status='done').order_by('-date')[:4]
    return render(request, 'main/index.html', {'done': done, 'counter': counter})


class RegisterView(CreateView):
    template_name = 'registration/signup.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
