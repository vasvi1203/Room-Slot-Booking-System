# Generated by Django 3.0.4 on 2020-04-03 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_auto_20200403_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_number1',
            new_name='room_number',
        ),
        migrations.RenameField(
            model_name='slot',
            old_name='time_end1',
            new_name='time_end',
        ),
        migrations.RenameField(
            model_name='slot',
            old_name='time_start1',
            new_name='time_start',
        ),
    ]
