# Generated by Django 3.2 on 2023-11-29 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_auto_20231129_0508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regis',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='regis',
            old_name='FullName',
            new_name='fullname',
        ),
        migrations.RenameField(
            model_name='regis',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='regis',
            old_name='PhoneNumber',
            new_name='phonenumber',
        ),
        migrations.AlterField(
            model_name='list',
            name='manufactured_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 29, 5, 36, 12, 220118)),
        ),
    ]