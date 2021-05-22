from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.

# post summary diplayed on the page index.html 
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

# blog posts in all the blog pages 
class PostPage(models.Model):
	title = Post.title
	author = models.CharField(max_length=100, default=User) #change it to the current logged in user
	introduction = models.TextField(default='Type your introduction here ...')
	content = models.TextField()
	
	quote = models.CharField(max_length=300, default='Quote from your blog here ...')
	
	titlePara1 = models.CharField(max_length=100, default='...') 
	para1 = models.TextField(default='...')

	para2 = models.TextField(default='...')

	titlePara3 = models.CharField(max_length=100, default='...') 
	para3 = models.TextField(default='...')
	
	date_posted = Post.date_posted

	def __str__(self):
		return self.title

#contact us form in the contact.html page
class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	website = models.URLField()
	message = models.TextField()

	def __str__(self):
		return 'message from '+ self.name
