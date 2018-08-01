from django.shortcuts import render
from event.models import Event

# Create your views here.


def event(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'event.html', locals())
