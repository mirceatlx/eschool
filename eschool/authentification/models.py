from django.db import models
from django.forms import ModelForm

# Create your models here.

class Student(models.Model):
    first = models.CharField(max_length = 64)
    last = models.CharField(max_length = 64)
    user = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)
    email = models.EmailField(primary_key = True)
    details = models.CharField(max_length = 200, blank = True)
    

    def __str__(self):
        return f"{self.first} {self.last} {self.email}"

class Parent(models.Model):
    first = models.CharField(max_length = 64)
    last = models.CharField(max_length = 64)
    user = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)
    email = models.EmailField(primary_key = True)
    details = models.CharField(max_length = 200, blank = True)
    students = models.ManyToManyField(Student, blank = True, related_name = 'parents')

    def __str__(self):
        return f"{self.first} {self.last} {self.email}"

class Teacher(models.Model):
    first = models.CharField(max_length = 64)
    last = models.CharField(max_length = 64)
    user = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)
    email = models.EmailField(primary_key = True)
    details = models.CharField(max_length = 200, blank = True)

    def __str__(self):
        return f"{self.first} {self.last} {self.email}"

class Class(models.Model):
    students = models.ManyToManyField(Student, blank = True, related_name = 'students')
    teachers = models.ManyToManyField(Teacher, blank = True, related_name = 'teachers')
    class_name = models.CharField(max_length = 3)

    def __str__(self):
        return f"{self.class_name}"

class Subject(models.Model):
    subject_name = models.CharField(max_length = 64)
    xclass = models.ForeignKey(Class, on_delete = models.CASCADE, related_name = 'xclass')

    def __str__(self):
        return f"{self.subject_name} in {self.xclass}"

class Document(models.Model):
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE, related_name = 'subjects')
    doc = models.FileField(upload_to = 'eschool')
    date = models.DateField()

class Assignment(models.Model):
    classn = models.ForeignKey(Class, on_delete = models.CASCADE, related_name = 'classes')
    date = models.DateTimeField()
    details = models.CharField(max_length = 200)
    doc = models.FileField(blank = True, upload_to = 'eschool')

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = 'grades')
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE, related_name = 'grades')
    grade = models.IntegerField()
    date = models.DateTimeField()

class Absence(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = 'absences')
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE, related_name = 'absences')
    date = models.DateTimeField()
    
class StudentFormUp(ModelForm):
    class Meta:
        model = Student
        fields = ['first', 'last', 'user', 'password', 'email', 'details']

class ParentFormUp(ModelForm):
    class Meta:
        model = Parent
        fields = ['first', 'last', 'user', 'password', 'email', 'details', 'students']

class StudentLog(ModelForm):
    class Meta:
        model = Student
        fields = ['email', 'password']

class ParentLog(ModelForm):
    class Meta:
        model = Parent
        fields = ['email', 'password']

class TeacherFormLog(ModelForm):
    class Meta:
        model = Teacher
        fields = ['email', 'password']