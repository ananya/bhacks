# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-03-09 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_user_info_facebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='facebook',
            field=models.CharField(default='facebook login', max_length=50),
        ),
    ]
