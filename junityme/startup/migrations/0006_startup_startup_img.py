# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-23 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0005_teambuild'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='startup_img',
            field=models.FileField(default='img', upload_to=''),
        ),
    ]
