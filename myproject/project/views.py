from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
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


@login_required
def profile(request):
    return render(request, 'main/profile.html')


class BBLoginView(LoginView):
    template_name = 'registration/login.html'


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
