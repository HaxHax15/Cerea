# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=64, verbose_name='Имя'),
        ),
    ]
