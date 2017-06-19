# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RescueInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6, verbose_name='이름')),
                ('age', models.IntegerField(verbose_name='나이')),
                ('burth', models.DateTimeField(verbose_name='생년월일')),
                ('address', models.CharField(blank=True, max_length=40, null=True, verbose_name='요약')),
                ('phone', models.CharField(blank=True, help_text="'-'없이 입력하세요 ex) 01012341234", max_length=11, null=True, verbose_name='연락처')),
                ('location', models.CharField(max_length=10, verbose_name='사고위치')),
                ('symptom', models.CharField(max_length=20, verbose_name='증상')),
                ('cause', models.CharField(max_length=30, verbose_name='원인')),
                ('content', models.TextField(verbose_name='구조 내용')),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
