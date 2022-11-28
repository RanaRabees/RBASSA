"""RBSA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Welcome To RBSA"
admin.site.site_title = "RBSA Data Base"
admin.site.index_title = "RBSA Data Base"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('form/', views.form, name='form'),
    path('fullview/', views.fullview, name='fullview'),
    path('formpy/', views.formpy, name='formpy'),
    path('BlackHole/', include('BlackHole.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
