from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'authentification/index.html')

def student(request):
    pass

def teacher(request):
    pass

def parent(request):
    pass