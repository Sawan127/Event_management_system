from django.db import models
from django.conf import settings
from events.models import Event

# Create your models here.
class Booking(models.Model):
    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    
    num_tickets = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='booked')
    
    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = self.event.price * self.num_tickets
            
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.user.username} - {self.event.title} ({self.num_tickets} tickets)"