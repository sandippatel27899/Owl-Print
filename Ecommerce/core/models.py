from django.db import models
from django.contrib.auth.models import User
from django.conf import settings




class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    short_description = models.TextField()
    image = models.ImageField()
    quantity = models.IntegerField(default=0)


    def __str__(self):
        return self.title


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)

    def  __str__(self):
        return self.user.username
    
    
