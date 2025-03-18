from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    national_id = models.CharField(max_length=11, unique=True)
    email = models.EmailField(null=True, blank=True) #optional


class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    national_id = models.CharField(max_length=11, unique=True)
    email = models.EmailField(null=True, blank=True) #optional


class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    has_pool = models.BooleanField(default=False)
    is_beachfront = models.BooleanField(default=False)
    has_entertainment = models.BooleanField(default=False)
    allows_pets = models.BooleanField(default=False)
    is_for_parties = models.BooleanField(default=False)
    owner =models.ForeignKey(to=Owner, on_delete=models.CASCADE)
    user =models.ForeignKey(to=User, on_delete=models.CASCADE)
