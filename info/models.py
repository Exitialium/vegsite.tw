from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Restaurants(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=200, default=uuid.uuid4, unique=True)
    description = models.CharField(max_length=10000)
    dirName = models.CharField(max_length=100,unique=True)
    address = models.CharField(max_length=1000,unique=True)
    mapUrl = models.CharField(max_length=10000,unique=True)
    imgUrl = ["//assets/images/tbd.png","//assets/images/tbd.png"]
    

    
    
    
