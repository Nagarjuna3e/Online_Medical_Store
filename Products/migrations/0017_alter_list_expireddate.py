# Generated by Django 3.2 on 2023-12-05 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0016_alter_list_expireddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='ExpiredDate',
            field=models.DateField(),
        ),
    ]
