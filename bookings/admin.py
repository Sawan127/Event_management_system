from django.contrib import admin
from .models import Booking

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'num_tickets', 'total_price', 'status', 'booking_date')
    list_filter = ('status', 'booking_date')
    search_fields = ('user__username', 'event__title')