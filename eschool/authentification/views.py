from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from .forms import *
from dashboard.views import *
# Create your views here.

def index(request):
    return render(request, 'authentification/index.html')

def student_login(request):
    if request.method == 'POST':
        form = LogIn(request.POST)
        if form.is_valid():
            if Student.objects.filter(email = form.cleaned_data['email']).exists():
                student = Student.objects.get(email = form.cleaned_data['email'])
                if student and student.password == form.cleaned_data['password']:
                    # login done
                    # goes to the main student dashboard
                    return redirect('student', form.cleaned_data['email'])
                else:
                    return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponseRedirect(reverse("index"))
    else:
        form = LogIn()
    return render(request, 'authentification/student.html', {'form' : form})

def teacher_login(request):
    if request.method == 'POST':
        form = LogIn(request.POST)
        if form.is_valid():
            if Teacher.objects.filter(email = form.cleaned_data['email']).exists():
                teacher = Teacher.objects.get(email = form.cleaned_data['email'])
                if teacher and teacher.password == form.cleaned_data['password']:
                    # login done
                    # goes to the main teacher dashboard
                    return redirect('teacher', form.cleaned_data['email'])
                else:
                    return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponseRedirect(reverse("index"))
    else:
        form = LogIn()
        return render(request, 'authentification/teacher.html', {'form': form})


def parent_login(request):
    if request.method == 'POST':
        form = LogIn(request.POST)
        if form.is_valid():
            if Parent.objects.filter(email = form.cleaned_data['email']).exists():
                parent = Parent.objects.get(email = form.cleaned_data['email'])
                if parent and parent.password == form.cleaned_data['password']:
                    # login done
                    # goes to the main parent dashboard
                    return redirect('parent', form.cleaned_data['email'])
                else:
                    return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponseRedirect(reverse("index"))
    else:
        form = LogIn()
    return render(request, 'authentification/parent.html', {'form' : form})

def student_signup(request):
    if request.method == 'POST':
        form = StudentFormUp(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            form.save()
            xss = Class.objects.get(class_name = instance.xclass)
            xss.students.add() # in the database!!
            return HttpResponseRedirect(reverse("student"))
        else:
            return HttpResponse("This user already exists!")

    else:
        form = StudentFormUp()
        return render(request, 'authentification/s_signup.html', {'form' : form})

def parent_signup(request):
    if request.method == 'POST':
        form = ParentFormUp(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("parent"))
        else:
            return HttpResponse("This user already exists!")
    else:
        form = ParentFormUp()
    return render(request, 'authentification/p_signup.html', {'form' : form})


