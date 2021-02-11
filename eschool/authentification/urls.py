from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('student/', views.student_login, name = "student"),
    path('teacher/', views.teacher_login, name = "teacher"),
    path('parent/', views.parent_login, name = "parent"),
    path('student/signup', views.student_signup, name = "student_signup"),
    path('parent/signup', views.parent_signup, name = "parent_signup"),

]