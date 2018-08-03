from django.shortcuts import render
from event.models import Event, EventImage

# Create your views here.


def event(request):
    events = Event.objects.all().order_by('-date')
    events_dict = [ {'name': event.name, 'cover': event.images.filter(is_cover=True)[:1]} for event in events]
    return render(request, 'event.html', locals())
