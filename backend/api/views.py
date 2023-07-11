from django.http import request
from django.http import HttpResponseRedirect
from django.shortcuts import render 



def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')


def cs(request):
    return render(request,'comingsoon.html')


