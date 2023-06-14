from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

# Create your models here.
class products(models.Model):
    category_choices = [
        ('head','head'),
        ('body','body'),
        ('foot','foot'),
        ('equip','equip'),
        ('more','more'),
    ]
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=1000,unique=True)
    description = models.TextField(max_length=1000000)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.CharField(max_length=1000,choices=category_choices)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="uploads/",null=True)
    phone_number = models.CharField(max_length=100000,default="0712345678")

class feedback(models.Model):
    email = models.EmailField()
    number = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000)
    