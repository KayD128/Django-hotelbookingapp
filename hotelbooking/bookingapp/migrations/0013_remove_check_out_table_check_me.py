# Generated by Django 4.0.5 on 2022-07-30 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0012_rename_check_in_check_out_table_check_me'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check_out_table',
            name='check_me',
        ),
    ]
