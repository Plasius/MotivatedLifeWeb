# Generated by Django 2.0.1 on 2018-01-09 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0008_auto_20180108_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='day',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]