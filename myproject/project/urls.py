from django.urls import path
from project import views
from .views import index, BBLoginView, profile, RegisterView, createaplication, aplication, delete
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', index, name='index'),
    path('login/', BBLoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', aplication, name='profile'),
    path('create_aplication/', createaplication, name='createaplication'),
    path('profile/<int:id>', views.delete, name='delete')
]
