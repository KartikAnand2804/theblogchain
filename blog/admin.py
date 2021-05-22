from django.contrib import admin
from .models import Post, PostPage, Contact

# Register your models here.
admin.site.register(Post)
admin.site.register(PostPage)
admin.site.register(Contact)