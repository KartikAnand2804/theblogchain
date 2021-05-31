from django.shortcuts import render, redirect
from django.contrib.admin import views as admin_view
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse

#create your models here
def register(request):
	if request.method == 'POST':
		#if 'login' in request.POST:
			
			# logging into existing account
		#	email = request.POST['loginEmail']
		#	password = request.POST['loginPassword']

		#	user = User

		#	if user:
		#		messages.success(request, 'successfully logged in.')
		#	else:
		#		messages.error(request, 'Invalid Login Credentials')
	
		if 'register' in request.POST:
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
			return HttpResponseRedirect(reverse('admin:index'))

		
	return render(request, 'users/register.html')

def profile(request):
	return render(request, 'users/profile.html')


