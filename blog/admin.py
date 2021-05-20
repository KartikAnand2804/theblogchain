from django.contrib import admin
from .models import Post, PostPage

# Register your models here.
admin.site.register(Post)
admin.site.register(PostPage)