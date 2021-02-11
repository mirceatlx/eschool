from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.

def student(request, email):
    return HttpResponse("Hello World!")

def teacher(request, email):
    return HttpResponse("Hello World!")

def parent(request, email):
    return HttpResponse("Hello World!")
