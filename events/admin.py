from django.contrib import admin
from .models import Event

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'venue', 'date_time', 'price', 'available_seats', 'created_by')
    search_fields = ('title', 'venue', 'category')
    list_filter = ('category', 'date_time')
    

