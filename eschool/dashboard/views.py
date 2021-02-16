from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from authentification.models import *


# Create your views here.

def student(request, email):
    student = Student.objects.get(email = email)
    return render(request, 'dashboard/student.html', {'student' : student}) 

def teacher(request, email):
    return HttpResponse("Hello World!")

def parent(request, email):
    return HttpResponse("qq")
