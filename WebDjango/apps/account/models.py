from django.db import models
from django.contrib.auth.models import User


class Animals(models.Model):
    animal_name = models.CharField(max_length=3)
    real_name = models.CharField(max_length=30, null=True)


class Roles(models.Model):
    role_name = models.CharField(max_length=20)
    real_name = models.CharField(max_length=30, null=True)


class UserInfo(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    town = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    patronymic = models.CharField(max_length=50, null=True)
    favourite_animals = models.ManyToManyField(Animals)
    role = models.ForeignKey(Roles, null=True, on_delete=models.DO_NOTHING)


class Subscribe(models.Model):
    mail = models.CharField(max_length=20)


class Question(models.Model):
    name = models.CharField(max_length=21)

class Quiz(models.Model):
    who = models.CharField(max_length=50, null=True)
    # school
    how_know = models.CharField(max_length=20, null=True)
    # type
    form = models.CharField(max_length=20, null=True)
    # form
    answer = models.ManyToManyField(Question)
