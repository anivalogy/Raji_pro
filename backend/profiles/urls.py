from django.urls import path ,include  
from . views import *
urlpatterns = [
    path('port',port,name='port'),
    path('projects',projects,name='projects'),
    path('blog',blog, name='blog'),
    path('resume',resume, name='resume'),
    path('callus',callus, name='callus'),
]