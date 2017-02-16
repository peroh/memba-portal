# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 06:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_of', to=settings.AUTH_USER_MODEL),
        ),
    ]