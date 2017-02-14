from __future__ import unicode_literals
import os
from django.db import models
# import members


# Create your models here.

class CourseType(models.Model):
    course_type = models.CharField(max_length=128)
    paperwork_template = models.FileField(upload_to='paperwork_templates', blank=True)

    def __str__(self):
        return self.course_type

class Course(models.Model):
    course_max_length = 128
    course_type = models.ForeignKey(CourseType)
    course_name = models.CharField(max_length=course_max_length)
    course_start_date = models.DateField(null=True, blank=True)
    course_end_date = models.DateField(null=True, blank=True)
    # trainer = models.ForeignKey('members.Member', related_name="trainer_set", blank=True)
    # assessor = models.ForeignKey('members.Member', related_name="assessor_set", blank=True)

    def __str__(self):
        return self.course_name

class PaperworkHistory(models.Model):
    paperwork = models.FileField()
    course = models.ForeignKey('Course')

    def __str__(self):
        return os.path.basename(self.paperwork.name)