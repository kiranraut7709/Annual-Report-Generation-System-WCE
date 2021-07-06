# Generated by Django 3.1.4 on 2021-05-17 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phd',
            name='department',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='phd',
            name='guide_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='phd',
            name='registration_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='phd',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='phd',
            name='completion_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='phd',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]