# Generated by Django 3.0.4 on 2020-03-12 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0004_auto_20200312_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='eventPoster',
        ),
    ]