# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 00:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0005_member_club'),
        ('awards', '0002_auto_20170221_0058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Awarded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, default=None, null=True)),
                ('end_date', models.DateField(blank=True, default=None, null=True)),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.Award')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Member')),
            ],
        ),
        migrations.AddField(
            model_name='award',
            name='members',
            field=models.ManyToManyField(through='awards.Awarded', to='members.Member'),
        ),
    ]