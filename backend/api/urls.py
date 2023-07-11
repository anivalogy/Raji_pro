from django.urls import path
from api.views import * 
urlpatterns = [
    path('',index,name='index'),
    path('home',home,name='home'),
]
