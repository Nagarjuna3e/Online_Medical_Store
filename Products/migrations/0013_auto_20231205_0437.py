# Generated by Django 3.2 on 2023-12-05 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0012_alter_list_manufactured_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='manufactured_at',
        ),
        migrations.AddField(
            model_name='list',
            name='ExpiredDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 4, 37, 16, 407711)),
        ),
    ]