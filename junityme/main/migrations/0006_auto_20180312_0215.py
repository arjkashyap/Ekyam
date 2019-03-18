# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-11 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180312_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='inc_address',
            field=models.TextField(default='Address', max_length=600),
        ),
        migrations.AlterField(
            model_name='details',
            name='inc_doc',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='details',
            name='inc_policy',
            field=models.FileField(upload_to=''),
        ),
    ]
