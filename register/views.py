from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import RegisterForm
# Create your views here.

def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			usern = response.POST["username"]
			passw = response.POST["password1"]
			user = authenticate(username=usern, password=passw)
			login(response, user)
			return redirect("/")
		return redirect("/register")
	else:
		form = RegisterForm()
	return render(response, "register/register.html", {"form":form})