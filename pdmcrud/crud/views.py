from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'pages/index.html')

# USERS views
def users(request):
    return render(request,'users/index.html')

def users_create(request):
    return render(request,'users/create.html')

def users_edit(request):
    return render(request,'users/edit.html')

def about(request):
    return render(request,'pages/about.html')
