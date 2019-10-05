# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-10-05 11:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0006_auto_20191005_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='question_like_user', to=settings.AUTH_USER_MODEL),
        ),
    ]