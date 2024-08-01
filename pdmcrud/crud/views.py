from django.shortcuts import render
from django.http import HttpResponse
# Import models
from .models import User

# Create your views here.

# INDEX view
def index(request):
    return render(request,'pages/index.html')

# USERS views
# Send all user data to USERS index page
def users(request):
    users = User.objects.all()
    return render(request,'users/index.html', {'users':users})

def users_create(request):
    return render(request,'users/create.html')

def users_edit(request):
    return render(request,'users/edit.html')

# ABOUT view
def about(request):
    return render(request,'pages/about.html')