from django.urls import path, include
from django.contrib.auth import views as auth_views
from project import views
from .views import index


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.RegisterView.as_view(), name='logout'),
    path('', views.index, name='index')
]
