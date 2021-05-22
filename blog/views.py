from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post, PostPage, Contact


# Create your views here.

def index(request):
	context = {'posts': Post.objects.all()
	}
	return render(request, 'blog/index.html', context)

def about(request):
	return render(request, 'blog/about.html')

def contact(request):
	if request.method == 'POST':	
		name = request.POST["cName"]
		email = request.POST["cEmail"]
		website = request.POST["cWebsite"]
		message = request.POST["cMessage"]
		
		contact = Contact(name=name, email=email, website=website, message=message)
		contact.save()

	return render(request, 'blog/contact.html')

def category(request):
	return render(request, 'blog/category.html')