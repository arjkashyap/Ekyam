# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-15 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_details_inc_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='incubator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='esc_key', to='main.Incubators'),
        ),
    ]
