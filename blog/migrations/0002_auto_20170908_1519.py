# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 07:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creat_time',
            new_name='created_time',
        ),
    ]
