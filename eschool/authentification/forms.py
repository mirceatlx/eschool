from django import forms

class LogIn(forms.Form):
    email = forms.EmailField(label = 'Email')
    password = forms.CharField(label = 'Password', max_length = 64)
