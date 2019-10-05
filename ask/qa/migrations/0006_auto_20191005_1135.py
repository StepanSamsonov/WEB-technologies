# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-10-05 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0005_auto_20191005_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]