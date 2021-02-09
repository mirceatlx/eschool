from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'authentification/index.html')

def student(request):
    return render(request, 'authentification/student.html')

def teacher(request):
    return render(request, 'authentification/teacher.html')

def parent(request):
    return render(request, 'authentification/parent.html')