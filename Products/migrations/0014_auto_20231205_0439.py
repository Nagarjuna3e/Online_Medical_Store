# Generated by Django 3.2 on 2023-12-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0013_auto_20231205_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='ExpiredDate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='list',
            name='MedicinePrice',
            field=models.CharField(max_length=250),
        ),
    ]
