"""blogchain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', blog_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('about/', blog_views.about, name='about'),
    path('contact/', blog_views.contact, name='contact'),
    path('category/', blog_views.category, name='category'),
    path('register/', user_views.register, name='register'),
    path('audio/', blog_views.audio, name='audio'),
    path('gallery/', blog_views.gallery, name='gallery'),
    path('video/', blog_views.video, name='video'),
    #path('guide/', blog_views.guide, name='guide'),
    path('standard/', blog_views.standard, name='standard'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
