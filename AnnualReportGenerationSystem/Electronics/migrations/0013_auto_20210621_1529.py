# Generated by Django 3.1.4 on 2021-06-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electronics', '0012_auto_20210621_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='guideforphd',
            name='academic_year',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='phd',
            name='academic_year',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]