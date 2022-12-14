# Generated by Django 4.0.5 on 2022-07-28 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_table',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('mail', models.EmailField(max_length=30, null=True)),
                ('check_in', models.DateField(null=True)),
                ('check_out', models.DateField(null=True)),
                ('check_out_time', models.TimeField(null=True)),
                ('number_of_adult', models.IntegerField(null=True)),
                ('number_of_children', models.IntegerField(null=True)),
                ('rooms', models.CharField(choices=[('Standard Room', 'Standard Room'), ('Double Standard Room', 'Double Standard Room'), ('Executive Rooms', 'Executive Rooms'), ('Deluxe Rooms', 'Deluxe Rooms'), ('Classic Suite', 'Classic Suite'), ('Presidential Suite', 'Presidential Suite')], max_length=60)),
                ('comment_given', models.TextField(null=True)),
                ('room_key', models.BigIntegerField(default='435', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room_table',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('rooms', models.CharField(choices=[('Standard Room', 'Standard Room'), ('Double Standard Room', 'Double Standard Room'), ('Executive Rooms', 'Executive Rooms'), ('Deluxe Rooms', 'Deluxe Rooms'), ('Classic Suite', 'Classic Suite'), ('Presidential Suite', 'Presidential Suite')], max_length=50)),
                ('number_of_rooms', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Check_out_table',
            fields=[
                ('check_id', models.AutoField(primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('mail', models.EmailField(max_length=30, null=True)),
                ('check_in', models.DateField(null=True)),
                ('check_out', models.DateField(null=True)),
                ('number_of_adult', models.IntegerField(null=True)),
                ('number_of_children', models.IntegerField(null=True)),
                ('rooms', models.CharField(choices=[('Standard Room', 'Standard Room'), ('Double Standard Room', 'Double Standard Room'), ('Executive Rooms', 'Executive Rooms'), ('Deluxe Rooms', 'Deluxe Rooms'), ('Classic Suite', 'Classic Suite'), ('Presidential Suite', 'Presidential Suite')], max_length=60)),
                ('key', models.BigIntegerField(default=0)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.booking_table')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.room_table')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='booking_table',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.room_table'),
        ),
        migrations.AddField(
            model_name='booking_table',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
