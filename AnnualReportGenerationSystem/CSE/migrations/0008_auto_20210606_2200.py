# Generated by Django 3.1.4 on 2021-06-06 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0007_auto_20210602_2356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='address1_permanant',
            new_name='address1_permanent',
        ),
    ]