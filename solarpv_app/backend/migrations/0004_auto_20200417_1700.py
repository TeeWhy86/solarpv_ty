# Generated by Django 3.0.5 on 2020-04-17 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200417_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cell',
            field=models.CharField(help_text='Enter as XXX-XXX-XXXX', max_length=60),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='sample@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='office',
            field=models.CharField(help_text='Enter as XXX-XXX-XXXX', max_length=60),
        ),
    ]
