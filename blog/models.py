from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
# general information 
class Info(models.Model):
	name = models.CharField(max_length=100, default="SharingInc.")
	email = models.EmailField(default="sharinginc.work@gmail.com")
	website = models.CharField(max_length=200, default="https://sharinginc.github.io/SharingInc/")
	about_us = models.TextField(default="about us content.")
	phone = models.CharField(max_length=10, default="9999999999")
	address = models.CharField(max_length=400, default="address content.")

	def __str__(self):
		return self.name

# post summary diplayed on the page index.html 
class Post(models.Model):
	id_num = models.CharField(max_length=3, default='000')
	tag = models.CharField(max_length=100, default='tag name')
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=320)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.CharField(max_length=100, default=User)

	def __str__(self):
		return self.title

# blog posts in all the blog pages 
class PostPage(models.Model):
	id_num = models.CharField(max_length=3, default='000')
	tag = models.CharField(max_length=100, default='tag name')
	title = models.CharField(max_length=200, default='title' )
	author = models.CharField(max_length=100, default=User) #change it to the current logged in user
	introduction = models.TextField(default='Type your introduction here ...')
	content = models.TextField()
	
	quote = models.CharField(max_length=300, default='Quote from your blog here ...')
	
	titlePara1 = models.CharField(max_length=100, default='...') 
	para1 = models.TextField(default='...')

	para2 = models.TextField(default='...')

	titlePara3 = models.CharField(max_length=100, default='...') 
	para3 = models.TextField(default='...')
	
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

#contact us form in the contact.html page
class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(default=9999999999, max_length=10)
	message = models.TextField()

	def __str__(self):
		return 'message from '+ self.name
