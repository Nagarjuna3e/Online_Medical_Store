# Generated by Django 3.2 on 2023-11-30 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0011_alter_list_manufactured_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='manufactured_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 30, 2, 28, 4, 325040)),
        ),
    ]
