from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from authentification.models import *

# Create your views here.

def xcl(request, name):
    return HttpResponse('hello world!')