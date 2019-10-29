# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-26 06:25
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0002_auto_20180326_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='activation_key',
            field=models.CharField(default=uuid.UUID('85cdae4c-30be-11e8-af8a-9840bb29ab05'), max_length=64, verbose_name='Activation key'),
        ),
    ]