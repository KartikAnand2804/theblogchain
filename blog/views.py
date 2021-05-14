from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.

def index(request):
	context = {'posts': Post.objects.all()
	}
	return render(request, 'blog/index.html', context)

def about(request):
	return render(request, 'blog/about.html')

def contact(request):
	return render(request, 'blog/contact.html')

def category(request):
	return render(request, 'blog/category.html')