# Generated by Django 3.2 on 2023-11-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0002_auto_20231130_0202'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('orderdetails', models.CharField(max_length=250)),
                ('phonenumber', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='pays',
        ),
    ]