# Generated by Django 4.0.5 on 2022-08-03 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0019_alter_booking_table_real_check_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_table',
            name='real_check_in',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking_table',
            name='real_check_out',
            field=models.DateField(null=True),
        ),
    ]
