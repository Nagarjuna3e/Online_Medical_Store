# Generated by Django 3.2 on 2023-11-24 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='manufactured_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 24, 3, 10, 14, 831141)),
        ),
    ]
