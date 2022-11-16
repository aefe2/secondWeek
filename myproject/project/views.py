from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Aplication
from project.forms import RegisterUserForm


def index(request):
    counter = Aplication.objects.filter(status='new').all().count()
    done = Aplication.objects.filter(status='done').order_by('-date')[:4]
    return render(request, 'main/index.html', {'done': done, 'counter': counter})


class BBLoginView(LoginView):
    template_name = 'registration/login.html'


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


@login_required
def createaplication(request):
    return render(request, 'main/create_aplication.html')


@login_required
def profile(request):
    return render(request, 'main/profile.html')


@login_required
def aplication(request):
    a_items = request.user.aplication_set.all()
    return render(request, 'main/profile.html', context={'a_items': a_items, })


@login_required
def delete(request, id):
    apl = Aplication.objects.filter(id=id)
    if request.method == 'POST':
        apl.delete()
        return redirect('profile')
    return render(request, 'main/profile.html')

# регистрация, вход, главная страница, профиль, заявка, создание заявки
