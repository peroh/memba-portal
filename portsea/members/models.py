from __future__ import unicode_literals

from django.db import models
from custom_user_official.models import MyUser

class Member(models.Model):
    user = models.OneToOneField('custom_user_official.MyUser', related_name='user_of', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
