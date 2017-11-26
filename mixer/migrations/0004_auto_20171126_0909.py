# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 09:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixer', '0003_auto_20171126_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mixtape',
            name='saved_users',
            field=models.ManyToManyField(blank=True, related_name='saved_mixtapes', to=settings.AUTH_USER_MODEL),
        ),
    ]