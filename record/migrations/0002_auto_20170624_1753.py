# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rescue',
            name='burth',
            field=models.DateField(null=True, verbose_name='생년월일'),
        ),
    ]
