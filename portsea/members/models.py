from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser

# from portsea.courses import models

# Create your models here.

class User(AbstractBaseUser):
    pass

class Profile(User):
    email = models.EmailField()
    user = models.OneToOneField('members.User', blank=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

# class MyUser()

# class Member(models.Model):
#     max_name_length = 128
#     user = models.OneToOneField(User)
#     email = models.EmailField(max_length=max_name_length)
#
# class MyUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#
#     USERNAME_FIELD = 'email'

