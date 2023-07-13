"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from home.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
    path('profiles/',include('profiles.urls')),


]





urlpatterns = [
    path('admin/', admin.site.urls),
    path('about',about,name='about'),
    path('services',services,name='services'),
    path('account',account,name='account'),
    path('BLOG',BLOG,name='BLOG'),
    path('coming_soon',coming_soon,name='coming_soon'),
    path('error',error,name='error'),
    path('main',main,name='main'),
    path('',main),
    path('price',price,name='price'),
    path('portfolio',portfolio,name='portfolio'),
    path('services',services,name='services'),
    path('contact',contact,name='contact'),
    path('profiles/',include('profiles.urls')),
    path('login',login,name="login"),
    path('logout',logout,name="logout"),
]
