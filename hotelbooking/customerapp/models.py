from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(unique=False, max_length=100, null=True)
    mail = models.CharField(unique=False, max_length=100, null=True)
    phone = models.CharField(unique=False, max_length=11, null=True)
    message = models.TextField(unique=False, max_length=100)
