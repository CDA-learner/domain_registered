# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_filed1_filed2_filed3'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered',
            name='Review_status',
            field=models.CharField(max_length=100, null=True, verbose_name='审核状态'),
        ),
    ]