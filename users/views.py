from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('email')
			messages.success(request, f'Account created for {email}!')
			return redirect('blog_views.index')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form': form})

def profile(request):
	return render(request, 'users/profile.html')
