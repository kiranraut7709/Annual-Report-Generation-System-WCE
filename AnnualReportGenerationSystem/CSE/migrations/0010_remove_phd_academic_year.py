# Generated by Django 3.2.3 on 2021-06-16 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0009_auto_20210614_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phd',
            name='academic_year',
        ),
    ]