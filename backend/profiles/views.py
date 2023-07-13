from django.shortcuts import render

# Create your views here.
def port(request):
    return render(request,'personal/index.html')




def projects(request):
    return render(request, 'personal/projects.html')


def resume(request):
    return render(request, 'personal/resume.html')


def blog(request):
    return render(request, 'personal/blog.html')


def callus(request):
    return render(request, 'personal/contacts.html')