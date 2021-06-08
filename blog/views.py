from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post, PostPage, Contact, Info
from django.contrib import messages


# Create your views here.

context = { 'posts': Post.objects.all(),
			'info': Info.objects.all(),
			'content': PostPage.objects.all()} 

def index(request):
	 # post summaries dictionary
	return render(request, 'blog/index.html', context)

def about(request):
	return render(request, 'blog/about.html', context)

def contact(request):
	if request.method == 'POST':	
		name = request.POST["cName"]
		email = request.POST["cEmail"]
		phone = request.POST["cNumber"]
		message = request.POST["cMessage"]
		
		contact = Contact(name=name, email=email, phone=phone, message=message)
		contact.save()
		messages.success(request, 'Message sent!')

	return render(request, 'blog/contact.html', context)

def category(request):
	return render(request, 'blog/category.html', context)

def audio(request):
	return render(request, 'blog/single-audio.html', context)

def gallery(request):
	return render(request, 'blog/single-gallery.html', context)

def video(request):
	return render(request, 'blog/single-video.html', context)

def standard(request):
	return render(request, 'blog/single-standard.html', context)

#def guide(request):
#	return render(request, 'blog/style-guide.html', postcontent)