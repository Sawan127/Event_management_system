from django.db import models
from django.conf import settings

# Create your models here.
class Event(models.Model):
    CATEGORY_CHOICES = [
        ('music', 'Music'),
        ('art', 'Art'),
        ('technology', 'Technology'),
        ('sports', 'Sports'),
        ('education', 'Education'),
        ('health', 'Health'),
        ('business', 'Business'),
        ('conference', 'Conference'),
        ('workshop', 'Workshop'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    venue = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='events_created'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.venue}"
    
    def book_seat(self, num_seats):
        """Reduce available seats when a booking is made."""
        if num_seats <= self.available_seats:
            self.available_seats -= num_seats
            self.save()
        else:
            raise ValueError("Not enough available seats")