# Generated by Django 3.0.4 on 2020-03-26 13:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time_start',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
