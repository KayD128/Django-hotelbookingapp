# Generated by Django 4.0.5 on 2022-07-29 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0009_alter_booking_table_room_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='check_out_table',
            old_name='real_check_out',
            new_name='potential_check_out',
        ),
    ]