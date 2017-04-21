# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_user_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Addresses.Place'),
        ),
    ]
