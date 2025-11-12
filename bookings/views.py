from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from events.models import Event
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

@login_required
def create_booking(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        seats = int(request.POST.get('seats', 1))
        if event.available_seats >= seats:
            booking = Booking.objects.create(
                user=request.user,
                event=event,
                seats_booked=seats,
                payment_status='Success'  # Simulated payment
            )
            event.available_seats -= seats
            event.save()
            return render(request, 'bookings/booking_confirmation.html', {'booking': booking})
        else:
            return render(request, 'bookings/error.html', {'message': 'Not enough seats available'})

@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/dashboard.html', {'bookings': bookings})
