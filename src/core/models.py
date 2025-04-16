from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username


class Plant(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="plants")
    title = models.CharField(max_length=200)
    description = models.TextField(default="", blank=True)
    genus = models.CharField(max_length=150,default="", blank=True)
    watering_info = models.TextField(default="", blank=True)
    soil_type = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.owner}"
    

class CachePlant(models.Model):
    title = models.CharField(max_length=255, unique=True)
    genus = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    soil_type = models.CharField(max_length=255, blank=True)
    watering_info = models.TextField(blank=True)
    last_fetched = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title