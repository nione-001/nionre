from django.db import models

class Account(models.Model):
    email = models.CharField(max_length=30)
    passw = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    mobno = models.CharField(max_length=12,default="100000000")
    addr = models.CharField(max_length=100,default="addr")

class ForgetPass(models.Model):
    email = models.CharField(max_length=30)
    rlink = models.CharField(max_length=30,default="hello")

class Hotel(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    hotel = models.CharField(max_length=40)
    food = models.CharField(max_length=30)
    cost = models.IntegerField()
    approxTime = models.IntegerField()

class CurrentOrders(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    email = models.CharField(max_length=30)
    time = models.IntegerField()
    food = models.CharField(max_length=100)
    cost = models.IntegerField()
    paymentMethod = models.CharField(max_length=30)

class AutoMate(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    email = models.CharField(max_length=30)
    timetoorder = models.IntegerField()
    food = models.CharField(max_length=100)
    cost = models.IntegerField()

class FinishedOrders(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    email = models.CharField(max_length=30,default=" ")
    review = models.IntegerField(default=12)
    complients = models.CharField(max_length=100,default=" ")


class Subscription(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    email = models.CharField(max_length=30)
    amountType = models.CharField(max_length=30)
    pending = models.IntegerField()
    wallet = models.IntegerField()

class HotelOwner(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    owner = models.CharField(max_length=30)
    hotelName = models.CharField(max_length=50)
    passw = models.CharField(max_length=30)
    addr = models.CharField(max_length=100)