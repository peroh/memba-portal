from __future__ import unicode_literals
import datetime
from django.utils.timezone import now


from django.db import models

class EventType(models.Model):
    type = models.CharField(max_length=128)

    def __str__(self):
        return self.type

class Event(models.Model):
    name = models.CharField(max_length=128)
    member_signup = models.ManyToManyField('custom_user_official.MyUser', through='events.EventSignup')
    date = models.DateField(null=True, blank=True, default=now)
    start_time = models.TimeField(null=True, blank=True, default=now)
    end_time = models.TimeField(null=True, blank=True, default=now)
    type = models.ForeignKey('events.EventType', null=True)

    def __str__(self):
        return self.name

class EventSignup(models.Model):
    event = models.ForeignKey('events.Event')
    member = models.ForeignKey('custom_user_official.MyUser')
    date = models.DateField(null=True, blank=True, default=now)
    start_time = models.TimeField(null=True, blank=True, default=now)
    end_time = models.TimeField(null=True, blank=True, default=now)

