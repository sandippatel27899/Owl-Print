from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=255,blank=True)
    price = models.FloatField(default=5.0)
    description = models.TextField()
    image = models.ImageField()
    qty = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} : {self.price} x {self.qty} "
