from django import forms

class NameForm(forms.Form):
    username = forms.CharField(label='password', max_length=100)
    password = forms.CharField(label='password', max_length=100)