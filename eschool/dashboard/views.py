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
    teacher = Teacher.objects.get(email = email)
    return render(request, 'dashboard/teacher.html', {'teacher' : teacher})

def parent(request, email):
    parent = Parent.objects.get(email = email)
    student = parent.students.get()
    return render(request, 'dashboard/parent.html', {'parent' : parent, 'student' : student})


# i like pizza