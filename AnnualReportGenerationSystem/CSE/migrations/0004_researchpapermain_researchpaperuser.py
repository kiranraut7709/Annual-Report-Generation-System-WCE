# Generated by Django 3.1.4 on 2021-05-24 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0003_btechstudentdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchPaperMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doi', models.CharField(default='', max_length=20)),
                ('type_of_publication', models.CharField(default='', max_length=20)),
                ('details_of_paper', models.CharField(default='', max_length=200)),
                ('author_name', models.CharField(default='', max_length=200)),
                ('publication_date', models.DateField(default=datetime.date.today)),
                ('department', models.CharField(default='', max_length=20)),
                ('area_of_research', models.CharField(default='', max_length=20)),
                ('publication_details', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchPaperUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doi', models.CharField(default='', max_length=20)),
                ('user', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
