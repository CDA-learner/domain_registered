# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_domain_filed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain_filed',
            name='filed1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='domain_filed',
            name='filed2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='domain_filed',
            name='filed3',
            field=models.CharField(max_length=100, null=True),
        ),
    ]