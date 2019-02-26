"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import xadmin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('books/', include('books.urls')),
    path('contact/', include('contact.urls')),
    path('register/', include('register.urls')),
    path('celeryapp/', include('celeryapp.urls')),
    path('xadmin/', xadmin.site.urls),
    path('admin/', admin.site.urls),
    path('hello/', views.display_meta),
    path('', views.api),
    path('vue/',TemplateView.as_view(template_name="index.html")),
]

xadmin.site.site_header = '管理系统'
xadmin.site.site_title = '管理系统'