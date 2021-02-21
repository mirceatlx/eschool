from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>/<str:email>', views.subject, name = "subject"),
    path('<str:email>', views.teacher, name = "teacher")
]