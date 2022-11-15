from django.urls import path, include
from django.contrib.auth import views as auth_views
from project import views
from .views import index, BBLoginView, profile, RegisterView
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', index, name='index'),
    path('login/', BBLoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
]
