"""
URL configuration for travel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from basicapp.views import index,pakage,contact_form,pakageDetails
from userApp.views import login,register
urlpatterns = [
    path('login', login, name='login'),
    path('', index, name='index'),
    path('pakage/<str:DestGet>/', pakage, name='pakage'),
    path('pakage', pakageDetails, name='pakageDetails'),
    path('contact', contact_form, name='contact_form'),
    path('register', register, name='register'),
    
    
    # path('register', register, name='register'),
    
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
