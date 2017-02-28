from __future__ import unicode_literals
from django.db import models
import os

from club.models import Club


class CourseType(models.Model):
    course_type = models.CharField(max_length=128)
    paperwork_template = models.FileField(upload_to='paperwork_templates',
                                          blank=True)

    def __str__(self):
        return self.course_type


class Course(models.Model):
    course_max_length = 128
    course_type = models.ForeignKey(CourseType)
    course_name = models.CharField(max_length=course_max_length)
    course_start_date = models.DateField(null=True, blank=True)
    course_end_date = models.DateField(null=True, blank=True)
    club = models.ForeignKey('club.Club', null=True, default=None)
    members = models.ManyToManyField('members.Member')

    def __str__(self):
        return self.course_name


class PaperworkHistory(models.Model):
    paperwork = models.FileField()
    course = models.ForeignKey('Course')

    def __str__(self):
        return os.path.basename(self.paperwork.name)