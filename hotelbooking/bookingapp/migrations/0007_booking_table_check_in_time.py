# Generated by Django 4.0.5 on 2022-07-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0006_rename_check_id_check_out_table_check_out_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_table',
            name='check_in_time',
            field=models.TimeField(null=True),
        ),
    ]
