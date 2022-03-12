from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm #This is a pre-built form
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta: #this has to be named Meta. This saves the register form into the user Database
		model = User 
		fields = ["username","email","password1","password2"]