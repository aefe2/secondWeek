from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Aplication, Category
from project.forms import RegisterUserForm, CreateAplForm


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
def createapl(request):
    if request.method == 'POST':
        form = CreateAplForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_id = request.user.pk
            form.save()
            return redirect('profile')
    else:
        form = CreateAplForm(initial={'author': request.user})
    context = {'form': form}
    return render(request, 'main/create_aplication.html', context)


@login_required
def profile(request):
    return render(request, 'main/profile.html')


@login_required
def delete(request, id):
    apl = Aplication.objects.filter(id=id).all()
    if request.method == 'POST':
        apl.delete()
        return redirect('profile')
    return render(request, 'main/profile.html')


# регистрация, вход, главная страница, профиль, заявка, создание заявки

# @login_required
# # def new_apl(request):
# #     # apl_new = Aplication.objects.filter(status='New').order_by('date')
# #     apl_new = Aplication.objects.filter(status='new').all()
# #     if apl_new:
# #         return render(request, 'main/profile_new.html', {'new': apl_new})
# #     return render(request, 'main/profile.html')
#
# @login_required
# def done_apl(request):
#     return render(request, 'main/profile.html')
#
# @login_required
# def received_apl(request):
#     return render(request, 'main/profile.html')


# def aplication_filter(request):
#     statuss = request.GET.get('status')
#     if statuss:
#         aplications = Aplication.objects.filter(count__gte=1, status=statuss)
#     else:
#         aplications = Aplication.objects.all()
#     return render(request, 'main/profile.html', context={'aplications': aplications, 'status': Aplication.status})

@login_required
def aplication_render(request):
    apl_items = request.user.aplication_set.all().order_by('-date')
    return render(request, 'main/profile.html', context={'apl_items': apl_items})


def apl_filter(request, status):
    apl_items = request.user.aplication_set.all().filter(status=status).order_by('-date')
    return render(request, 'main/profile.html', context={'apl_items': apl_items, 'status': status})



# !!!!!!!!!!!!!!!!!!!!def apl_filter(self, status):
#     if self.GET.get('status') is not None:
#         apl_items = Aplication.objects.all()
#         if status == 'new':
#             return render(self, 'main/profile.html', context={'apl_tems': apl_items, 'status': status})
#     return render(self, 'main/profile.html')

# def apl_filter(self, status):
#     apl_items = self.GET.get('status')
#     if apl_items == 'done':
#         apl_items = Aplication.objects.filter(status=status)
#         print(1)
#     else:
#         apl_items = Aplication.objects.filter()
#         print(2)
#
#     return render(self, 'main/profile.html', context={
#         'status': status, 'apl_items': apl_items
#     })
