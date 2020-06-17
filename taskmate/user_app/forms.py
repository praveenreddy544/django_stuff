from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    #email = forms.EmailField()
    #fname = forms.CharField(max_length=30, required=False)
    #lname = forms.CharField(max_length=30, required=False)
    

    class Meta:
        model = User
        #fields = ['username','email','firstname','lastname','password1','password2',]
        fields = ['username','email','password1','password2','first_name','last_name']