from django.urls import path
from . import views

urlpatterns = [
    path('<str:email>/student', views.student, name = "student"),
    path('<str:email>/teacher', views.teacher, name = "teacher"),
    path('<str:email>/parent', views.parent, name = "parent"),

]