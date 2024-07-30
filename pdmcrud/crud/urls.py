from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='users'),
    path('users/create', views.users_create, name='users_create'),
    path('users/edit', views.users_edit, name='users_edit'),
    path('about', views.about, name='about'),
]