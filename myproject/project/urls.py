from django.urls import path, include

from project import views

urlpatterns = [
    path('login', views.login),
]
