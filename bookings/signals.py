from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Booking
from events.models import Event
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=Booking)
def update_event_seats_on_booking(sender, instance, created, **kwargs):
    """Reduce available seats when a booking is created."""
    event = instance.event
    if created and instance.status == 'booked':
        if event.available_seats >= instance.num_tickets:
            event.available_seats -= instance.num_tickets
            event.save()
        else:
            raise ValueError("Not enough available seats for this booking")
        
        ## Handle cancellation case
    elif not created and instance.status == 'cancelled':
        event.available_seats += instance.num_tickets
        event.save()
        
@receiver(pre_delete, sender=Booking)
def restore_seats_on_delete(sender, instance, **kwargs):
    """Restore seats when a booking is deleted."""
    event = instance.event
    if instance.status == 'booked':
        event.available_seats += instance.num_tickets
        event.save()
        

@receiver(post_save, sender=Booking)
def send_booking_confirmation_email(sender, instance, created, **kwargs):
    """Send an email to user upon successful booking."""
    if created and instance.status == 'booked':
        subject = f"Booking Confirmation for {instance.event.title}"
        message = (
            f"Hi {instance.user.username},\n\n"
            f"Your booking for the event '{instance.event.title}' "
            f"has been confirmed.\n\n"
            f"Event Details:\n"
            f"Date: {instance.event.date_time}\n"
            f"Location: {instance.event.venue}\n"
            f"Tickets: {instance.num_tickets}\n"
            f"Total Price: ₹{instance.total_price}\n\n"
            f"Thank you for booking with us!"
        )
        
        recepient = [instance.user.email]
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recepient,
            fail_silently=False,
        )
        
    elif not created and instance.status == 'cancelled':
        subject = f"Booking Cancelled - {instance.event.title}"
        message = (
            f"Hi {instance.user.username},\n\n"
            f"Your booking for '{instance.event.title}' has been cancelled.\n\n"
            f"Refunds (if applicable) will be processed soon.\n\n"
            f"Thanks,\nEvent Booker Team"
        )
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [instance.user.email]
        )