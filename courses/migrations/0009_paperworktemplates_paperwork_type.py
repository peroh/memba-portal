# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20170306_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='paperworktemplates',
            name='paperwork_type',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
