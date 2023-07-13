from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from django.http import HttpResponse


from .models import *


def login(request):
    return render(request,'login.html')


def logout(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')





































# Create your views here.
def home(request):
    
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def account(request):
    return render(request,'account.html')

def BLOG(request):
    return render(request,'blog.html')

def coming_soon(request):
    return render(request,'coming_soon.html')

def error(request):
    return render(request,'error.html')





def portfolio(request):
    return render(request,'portfolio.html')


def price(request):
    return render(request,'price.html')






































































def services(request):
    return render(request, 'services.html',)
































































































































































def main(request):  
    return render(request, 'main.html')



def contact(request):
    return render(request,'contact.html')