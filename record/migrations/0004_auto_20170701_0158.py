# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_rescue_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rescue',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='날짜'),
        ),
    ]
