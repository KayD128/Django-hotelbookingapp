from django.db import models
from django.contrib.auth.models import User
from numpy import random

# Create your models here.

room_type = [
    ("Standard Room", "Standard Room"),
    ("Double Standard Room", "Double Standard Room"),
    ("Executive Room", "Executive Room"),
    ("Deluxe Room", "Deluxe Room"),
    ("Classic Suite", "Classic Suite"),
    ("Presidential Suite", "Presidential Suite"),
]

class Room_table(models.Model):
    room_id = models.AutoField(primary_key=True)
    # booking = models.ForeignKey(Booking_table, on_delete=models.CASCADE)
    rooms = models.CharField(choices=room_type, unique=False, max_length=50)
    number_of_rooms = models.IntegerField(unique=False, default=0)
    room_price = models.BigIntegerField(unique=False, default=0)
    
class Booking_table(models.Model):
    # pin = str(random.randint(0000, 9999))

    booking_id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(unique=False, max_length=15, null=True)
    first_name = models.CharField(unique=False, max_length=50, blank=True)
    last_name = models.CharField(unique=False, max_length=50, blank=True)
    mail = models.EmailField(unique=False, max_length=30, null=True)
    potential_check_in = models.DateField(null=True, unique=False)
    real_check_in = models.DateField(null=True, unique=False)
    potential_check_out = models.DateField(null=True, unique=False)
    real_check_out = models.DateField(null=True, unique=False)
    check_in_time = models.TimeField(null=True, unique=False)
    check_out_time = models.TimeField(null=True, unique=False)
    number_of_adult = models.IntegerField(null=True, unique=False)
    number_of_children = models.IntegerField(null=True, unique=False)
    rooms = models.CharField(choices=room_type, unique=False, max_length=60)
    comment_given = models.TextField(unique=False, null=True)
    room_key = models.BigIntegerField(unique=False)
    room = models.ForeignKey(Room_table, on_delete=models.CASCADE)
    room_price = models.BigIntegerField(unique=False, default=0)
    total_price = models.BigIntegerField(unique=False, default=0)
     
class Check_in_table(models.Model):
    check_in_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(unique=False, max_length=15, null=True)
    first_name = models.CharField(unique=False, max_length=50, blank=True)
    last_name = models.CharField(unique=False, max_length=50, blank=True)
    mail = models.EmailField(unique=False, max_length=30, null=True)
    potential_check_in = models.DateField(unique=False)
    potential_check_out = models.DateField(null=True, unique=False)
    number_of_adult = models.IntegerField(null=True, unique=False)
    number_of_children = models.IntegerField(null=True, unique=False)
    rooms = models.CharField(choices=room_type, unique=False, max_length=60)
    key = models.BigIntegerField(default=0000, unique=False)
    room = models.ForeignKey(Room_table, on_delete=models.CASCADE)

class Check_out_table(models.Model):
    check_out_id = models.AutoField(primary_key=True)
    book_me = models.ForeignKey(Booking_table, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(unique=False, max_length=15, null=True)
    first_name = models.CharField(unique=False, max_length=50, blank=True)
    last_name = models.CharField(unique=False, max_length=50, blank=True)
    mail = models.EmailField(unique=False, max_length=30, null=True)
    real_check_in = models.DateField(null=True, unique=False)
    potential_check_out = models.DateField(null=True, unique=False)
    number_of_adult = models.IntegerField(null=True, unique=False)
    number_of_children = models.IntegerField(null=True, unique=False)
    rooms = models.CharField(choices=room_type, unique=False, max_length=60)
    key = models.BigIntegerField(default=0000, unique=False)
    room = models.ForeignKey(Room_table, on_delete=models.CASCADE)
