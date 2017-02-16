# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 23:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
        ('custom_user_official', '0003_myuser_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='club',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='club.Club'),
        ),
    ]