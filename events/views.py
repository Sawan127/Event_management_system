from django.shortcuts import render, get_object_or_404
from .models import Event

# Create your views here.
def event_list(request):
    event = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': event})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})