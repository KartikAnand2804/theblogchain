from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post, PostPage, Contact
from django.contrib import messages


# Create your views here.

postcontent = {'content': PostPage.objects.all()} # post pages dictionary

def index(request):
	context = {'posts': Post.objects.all()} # post summaries dictionary
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
		messages.success(request, 'Message sent!')

	return render(request, 'blog/contact.html')

def category(request):
	return render(request, 'blog/category.html')

def audio(request):
	return render(request, 'blog/single-audio.html', postcontent)

def gallery(request):
	return render(request, 'blog/single-gallery.html', postcontent)

def video(request):
	return render(request, 'blog/single-video.html', postcontent)

#def guide(request):
#	return render(request, 'blog/style-guide.html', postcontent)

def standard(request):
	return render(request, 'blog/single-standard.html', postcontent)
