# Generated by Django 3.0.5 on 2020-05-01 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solarpvsite', '0004_auto_20200501_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teststandard',
            name='publishdate',
            field=models.DateField(),
        ),
    ]
