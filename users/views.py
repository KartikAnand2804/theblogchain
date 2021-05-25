from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

#create your models here

def register(request):
	if request.method == 'POST':
		if 'login' in request.POST:
			# logging into existing account
			email = request.POST['loginEmail']
			password = request.POST['loginPassword']

			LoginUser = authenticate(request, email=email, password=password)

			if LoginUser is not None:
				return render(request, 'admin/')
			else:
				messages.error(request, 'Invalid Login Credentials')
	
		elif 'register' in request.POST:
			username = request.POST['username']
			Email = request.POST['email']
			password = request.POST['password']
			firstname = request.POST['firstName']
			lastname = request.POST['lastName']

			user = User.objects.create_user(username=username, email=Email, password=password)
			user.first_name = firstname
			user.last_name = lastname
			
			user.save()
			messages.success(request, 'Registered successfully. Login to your Account')

		
	return render(request, 'users/register.html')

def profile(request):
	return render(request, 'users/profile.html')


