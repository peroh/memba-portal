from __future__ import unicode_literals

from django.db import models

class Award(models.Model):
    award_name = models.CharField(max_length=128)
    # members = models.ManyToManyField('myuser.MyUser' ,through='awards.Awarded')
    members = models.ManyToManyField('members.Member', through='awards.Awarded')

    def __str__(self):
        return self.award_name

class Awarded(models.Model):
    award = models.ForeignKey('awards.Award')
    # member = models.ForeignKey('myuser.MyUser')
    member = models.ForeignKey('members.Member')
    start_date = models.DateField(null=True, blank=True, default=None)
    end_date = models.DateField(null=True, blank=True, default=None)
