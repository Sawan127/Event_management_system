from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('organizer', 'Organizer'),
        ('attendee', 'Attendee'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='attendee')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"