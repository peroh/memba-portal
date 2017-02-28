from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import now


class EventType(models.Model):
    type = models.CharField(max_length=128)

    def __str__(self):
        return self.type


class Event(models.Model):
    name = models.CharField(max_length=128)
    member_signup = models.ManyToManyField('members.Member',
                                           through='events.EventSignup')
    date = models.DateField(null=True, blank=True, default=now)
    start_time = models.TimeField(null=True, blank=True, default=now)
    end_time = models.TimeField(null=True, blank=True, default=now)
    type = models.ForeignKey('events.EventType', null=True)

    def __str__(self):
        return self.name


class EventSignup(models.Model):
    event = models.ForeignKey('events.Event')
    member = models.ForeignKey('members.Member')
    signup_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.event, self.member)
