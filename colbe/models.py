from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('available', 'موجود'),
    ('rented', 'اجاره داده شده'),
]


class Owner(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    national_id = models.CharField(max_length=11, unique=True)
    email = models.EmailField(null=True, blank=True) #optional


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20)
#     national_id = models.CharField(max_length=11, unique=True)
#     email = models.EmailField(null=True, blank=True) #optional


class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    has_pool = models.BooleanField(default=False)
    is_beachfront = models.BooleanField(default=False)
    has_entertainment = models.BooleanField(default=False)
    allows_pets = models.BooleanField(default=False)
    is_for_parties = models.BooleanField(default=False)
    image = models.ImageField(upload_to="colbe", null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    location = models.CharField(max_length=100, default='Tehran')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    owner =models.ForeignKey(to=Owner, on_delete=models.CASCADE, related_name="owner_colbe")
    user =models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_colbe")

class Rent(models.Model):
    '''
    برای ثبت درخواست نیاز به ایجاد یک کلاس جدید بود
    '''
    place = models.ForeignKey(to=Place, on_delete=models.CASCADE, related_name="place_colbe_rent")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_place_colbe")
    Owner = models.ForeignKey(to=Owner, on_delete=models.CASCADE, related_name="owner_place_colbe")
    start_date = models.DateField()
    end_date = models.DateField()
    payment = models.BooleanField()