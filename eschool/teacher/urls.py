from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>/<str:sub>/classroom', views.xcl, name = "xcl"),
    path('<str:email>/<str:subject>/<str:c>/student', views.student, name = "student"),
    path('<str:x>/<str:s>/addassignment', views.assignment, name = "assignment"),
    path('<str:s>/<str:x>/addtask', views.task, name = "task")
]