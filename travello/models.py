from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Destination(models.Model):

    name=models.CharField(max_length=50,null=True)
    person = models.IntegerField(null=True)
    description=models.CharField(max_length=50,null=True)
    price=models.IntegerField(null=True)
    image=models.ImageField(upload_to='pics',null=True,blank=True)
    off=models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    profilePicture = models.ImageField(upload_to='pics', null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer =models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    destination =models.ForeignKey(Destination,null=True,on_delete=models.SET_NULL)
    orderCount= models.IntegerField(null=True)
    totalOrderCost= models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.customer.name + ' : ' + self.destination.name