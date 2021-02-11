from django.urls import path
from . import views

urlpatterns = [
    path('<str:email>', views.student, name = "student"),
    path('<str:email>', views.teacher, name = "teacher"),
    path('<str:email>', views.parent, name = "parent"),

]