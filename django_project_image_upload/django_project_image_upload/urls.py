"""
URL configuration for django_project_image_upload project.

This file defines the URL patterns for your Django project.
It maps URL requests to their corresponding views, which handle the logic
for generating responses.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name='home')
Class-based views
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin # Import the Django admin module
from django.urls import path # Import the path function for defining URL patterns
from app_image_upload import views # Import the views from your app

urlpatterns = [
    path('admin/', admin.site.urls), # URL for Django admin interface
    # This URL maps to the index view in your app
    # The name='index' argument allows you to reference this URL by name in your templates or code
    path('', views.index, name='index'), # URL for the index page (root URL)
    # This URL maps to the success_page view in your app
    # The name='success_page' argument allows you to reference this URL by name in your templates or code
    path('success/', views.success_page, name='success_page'), # URL for the success page after image upload
]