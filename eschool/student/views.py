from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from authentification.models import *

# Create your views here.

def subject(request, name, email):
    student = Student.objects.get(email = email)
    subject = Subject.objects.get(subject_name = name)
    
    grades = Grade.objects.filter(student = student, subject = subject)
    grad = []
    for grade in grades:
        grad.append(grade.grade)
    
    absx = Absence.objects.filter(student = student, subject = subject)
    xabs = []
    for a in absx:
        xabs.append(a.date)

    return render(request, 'student/subject.html', 
        {'student' : student, 
         'subject' : subject,
         'grades' : grades, 
         'absences' : absx})

def teacher(request, email):
    teacher = Teacher.objects.get(email = email)
    return render(request, 'student/teacher.html', {'teacher' : teacher})