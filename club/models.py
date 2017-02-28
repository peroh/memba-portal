from __future__ import unicode_literals

from django.db import models


class Club(models.Model):
    club_name = models.CharField(max_length=128)

    def __str__(self):
        return self.club_name