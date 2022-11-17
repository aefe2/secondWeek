from django.urls import path
from project import views
from .views import index, BBLoginView, profile, RegisterView, createapl, aplication_render
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', index, name='index'),
    path('login/', BBLoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', aplication_render, name='profile'),
    path('create_aplication/', createapl, name='createapl'),
    path('profile/<int:id>', views.delete, name='delete'),
    path('profile/new', views.aplication_new, name='filter_new'),
    path('profile/done', views.aplication_done, name='filter_done'),
    path('profile/received', views.aplication_received, name='filter_received'),

]

