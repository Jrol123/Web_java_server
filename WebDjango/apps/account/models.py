from django.db import models
from django.contrib.auth.models import User


class Animals(models.Model):
    animal_name = models.CharField(max_length=15)


class Roles(models.Model):
    role_name = models.CharField(max_length=50)


class UserInfo(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    town = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    patronymic = models.CharField(max_length=50, null=True)
    favourite_animals = models.ManyToManyField(Animals)


class Subscribe(models.Model):
    mail = models.CharField(max_length=20)
