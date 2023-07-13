from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.

# Create your models here.
class Photo(models.Model):
    width = models.IntegerField(default = 0)
    height = models.IntegerField(default = 0)
    title = models.CharField(max_length = 200,null= True, blank = True)
    desc=models.TextField(null= True, blank = True)
    image = models.ImageField(null= True, blank = True, width_field="width", height_field="height")
    #Brand
    title1 = models.CharField(max_length = 200,null= True, blank = True)
    desc1=models.TextField(null= True, blank = True)
    image1 = models.ImageField(null= True, blank = True, width_field="width", height_field="height")
    #design
    title2 = models.CharField(max_length = 200,null= True, blank = True)
    desc2=models.TextField(null= True, blank = True)
    image2= models.ImageField(null= True, blank = True, width_field="width", height_field="height")
    #video
    title3 = models.CharField(max_length = 200,null= True, blank = True)
    desc3=models.TextField(null= True, blank = True)
    image3= models.ImageField(null= True, blank = True, width_field="width", height_field="height")

def __unicode__(self):
    return self.title

def __unicode__(self):
    return self.title1

def __unicode__(self):
    return self.title2

def __unicode__(self):
    return self.title3

def __unicode__(self):
    return self.title4



class Services(models.Model):
    img=models.ImageField()
    title = models.CharField(max_length = 50,null= True, blank = True)
    desc=models.TextField(null= True, blank = True)
    
#creating heading model for services pages
class Services_heading(models.Model):
    img = models.ImageField(null=True, blank=True)
    heading = models.CharField(max_length=50, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    
class team(models.Model):
    img = models.ImageField(null=True, blank=True)
    heading = models.CharField(max_length=50, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)