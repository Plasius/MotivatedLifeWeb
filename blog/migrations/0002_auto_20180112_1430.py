# Generated by Django 2.0.1 on 2018-01-12 12:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='timestamp',
            new_name='created',
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
