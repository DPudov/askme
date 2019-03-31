from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(label='Your login', max_length=100)