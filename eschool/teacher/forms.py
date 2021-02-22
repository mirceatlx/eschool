from django import forms
import datetime

class GradeForm(forms.Form):
    grade = forms.IntegerField(label = 'grade')

class AbsenceForm(forms.Form):
    absence = forms.DateTimeField(label = 'date', initial = datetime.datetime.now())

class AssignmentForm(forms.Form):
    date = forms.DateTimeField(label = 'date', initial = datetime.datetime.now())
    details = forms.CharField(label = 'details', max_length = 200)

class TaskForm(forms.Form):
    task = forms.CharField(label = 'task', max_length = 255)
    date = forms.DateTimeField(label = 'date', initial = datetime.datetime.now())