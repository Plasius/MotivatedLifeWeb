# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 09:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0006_auto_20171211_1825'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserQuoteProfile',
            new_name='QuoteProfile',
        ),
    ]
