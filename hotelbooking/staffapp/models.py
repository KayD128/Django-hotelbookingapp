from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    countries = [
        ("Nigeria", "Nigeria"),
        ("United States of America", "USA"),
        ("Ghana", "Ghana"),
        ("Niger", "Niger"),
        ("Germany", "Germany"),
        ("United Arab Emirates", "UAE")
    ]

    states = [
        ("Oyo", "Oyo"),
        ("Abuja", "Abuja")
    ]

    position = [
        ("General Manager", "GM"),
        ("Assistant General Manager", "AGM"),
        ("Front Office Manager", "FOM"),
        ("Concierge", "Concierge"),
        ("Guest Service Agent", "GSA"),
        ("Night Auditor", "Night Auditor"),
        ("Security", "Security"),
        ("Bellman", "Bellman"),
        ("Director of Sales", "DOS"),
        ("Sales Manager", "SM"),
        ("Sales Coordinator", "SC"),
        ("Catering Assistant", "Catering Assistant"),
        ("Executive Housekeeper", "Executive Housekeeper"),
        ("Assistant Executive Housekeeper", "Assistant Executive Housekeeper"),
        ("Continental Breakfast Attendant", "Continental Breakfast Attendant"),
        ("Houseperson", "Houseperson"),
        ("Room Attendant", "Room Attendant"),
        ("Chief Maintenance Engineer", "Chief Maintenance Engineer"),
        ("Assistant Maintenance", "Assistant Maintenance"),
    ]

    marital_status = [
        ("Single", "Single"),
        ("Married", "Married"),
        ("Divorced", "Divorced"),
        ("Complicated", "Complicated")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(unique=False, max_length=100,null=True)
    address = models.CharField(unique=False, max_length=100, null=True)
    phone = models.CharField(unique=False, max_length=11, null=True)
    nationality = models.CharField(choices=countries, max_length=100, unique=False, null=True)
    state = models.CharField(choices=states, max_length=20, unique=False, null=True)
    means_of_identity = models.ImageField(upload_to='pictures/', unique=False, null=True)
    particulars = models.FileField(upload_to='documents/', unique=False, null=True)
    profile_passport = models.ImageField(upload_to='staffs/', unique=False, null=True)
    position = models.CharField(choices=position, unique=False, max_length=100, null=True)
    marital_status = models.CharField(choices=marital_status, unique=False, max_length=20, null=True)
    staff = models.BooleanField(unique=False, default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

