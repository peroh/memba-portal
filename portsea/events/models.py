from __future__ import unicode_literals
import datetime
from django.utils.timezone import now


from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=128)
    member_signup = models.ManyToManyField('custom_user_official.MyUser', through='events.EventSignup')

    def __str__(self):
        return self.event_name

class EventSignup(models.Model):
    event = models.ForeignKey('events.Event')
    member = models.ForeignKey('custom_user_official.MyUser')
    date = models.DateField(null=True, blank=True, default=now)

