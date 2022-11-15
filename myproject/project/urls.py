from django.urls import path, include
from django.contrib.auth import views as auth_views
from project import views
from .views import index, BBLoginView, profile

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', BBLoginView.as_view(), name='login'),
    path('logout/', BBLoginView.as_view(), name='logout'),
    path('register/', BBLoginView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
]
