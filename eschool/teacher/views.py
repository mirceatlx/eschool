from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from authentification.models import *
import datetime
from .forms import *

# Create your views here.

def xcl(request, name, sub):
    x = Class.objects.get(class_name = name)
    sub = Subject.objects.get(subject_name = sub)
    return render(request, 'teacher/class.html', {'xcl' : x, 'subject' : sub})

def student(request, email, subject, c):

    s = Student.objects.get(email = email)
    cl = Class.objects.get(class_name = c)
    sub = Subject.objects.get(subject_name = subject, xclass = cl)

    if request.method == 'POST':
        form_grade = GradeForm(request.POST)
        form_absence = AbsenceForm(request.POST)
        if form_grade.is_valid():
            g = Grade(student = s, subject = sub, grade = form_grade.cleaned_data['grade'], date = datetime.datetime.now())
            g.save()
            # add to database
        if form_absence.is_valid():
            a = Absence(student = s, subject = sub, date = form_absence.cleaned_data['absence'], motivated = False)
            a.save()
            # add to database
        return HttpResponseRedirect("")

    else:   
        form_grade = GradeForm()
        form_absence = AbsenceForm()
        gr = Grade.objects.filter(student = s, subject = sub)
        avg = 0
        for g in gr:
            avg = avg + g.grade
        if gr.count() != 0:
            avg = avg / gr.count()
    return render(
        request, 
        'teacher/student.html', 
        {'student' : s, 
        'subject' : sub, 'x' : c, 'avg' : avg, 'form_grade' : form_grade, 'form_absence' : form_absence})

def assignment(request, x, s):

    cl = Class.objects.get(class_name = x)
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            ass = Assignment(classn = cl, date = datetime.datetime.now(), details = form.cleaned_data['details'])
            ass.save()
            # add to database
        return redirect('teacher:xcl', x, s)
    else:
        form = AssignmentForm()
    return render(request, 'teacher/assignment.html', {'x' : cl, 'form' : form})

def task(request, s, x):
    cl = Class.objects.get(class_name = x)
    sub = cl.subjects.get(subject_name = s) 
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Document(subject = sub, task = form.cleaned_data['task'], date = form.cleaned_data['date'])
            task.save()
        return redirect('teacher:xcl', x, s)
    else:
        form = TaskForm()
    return render(request, 'teacher/task.html', {'form' : form})