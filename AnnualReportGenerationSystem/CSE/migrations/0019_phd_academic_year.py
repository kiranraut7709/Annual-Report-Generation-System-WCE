# Generated by Django 3.1.4 on 2021-06-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0018_rename_eventconductedordelivered_eventconductedorattended'),
    ]

    operations = [
        migrations.AddField(
            model_name='phd',
            name='academic_year',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
