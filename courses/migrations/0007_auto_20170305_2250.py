# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 22:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_paperworkhistory_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperworkhistory',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]