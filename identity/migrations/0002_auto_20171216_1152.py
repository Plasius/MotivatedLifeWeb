# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 09:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserIdentityProfile',
            new_name='IdentityProfile',
        ),
    ]
