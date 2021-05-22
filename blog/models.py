from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

class PostPage(models.Model):
	title = Post.title
	content = models.TextField()
	date_posted = Post.date_posted

	def __str__(self):
		return self.title

class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	website = models.URLField()
	message = models.TextField()

	def __str__(self):
		return 'message from '+ self.name
