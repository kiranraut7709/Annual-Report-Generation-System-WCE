# Generated by Django 3.2.3 on 2021-06-16 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Electronics', '0004_auto_20210616_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phd',
            name='academic_year',
        ),
    ]
