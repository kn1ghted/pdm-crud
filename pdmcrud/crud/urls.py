from django.urls import path

# Import application views
from . import views

# Import application settings
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='users'),
    path('users/create', views.users_create, name='users_create'),
    path('users/edit', views.users_edit, name='users_edit'),
    path('about', views.about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)