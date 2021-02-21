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
    x = student.xclass
    avgs = []
    for sub in x.subjects.all():
        gr = Grade.objects.filter(student = student, subject = sub)
        avg = 0
        for g in gr:
            avg = avg + g.grade
        if gr.count() != 0:
            #print(gr.count)
            avg = avg / gr.count()
            avgs.append((avg,sub.subject_name))

    return render(request, 'dashboard/parent.html', {'parent' : parent, 'student' : student, 'avgs' : avgs})


