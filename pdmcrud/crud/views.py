from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm

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
    # POST http request and FILES for images
    form = UserForm(request.POST or None, request.FILES or None)
    # if form is valid, save details and redirect to users index page
    if form.is_valid():
        form.save()
        return redirect('users')
    return render(request,'users/create.html', {'form':form})

def users_edit(request):
    return render(request,'users/edit.html')

def users_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('users')

# ABOUT view
def about(request):
    return render(request,'pages/about.html')