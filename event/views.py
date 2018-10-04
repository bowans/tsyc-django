from django.http import Http404
from django.shortcuts import render
from event.models import Event
from event.serializers import EventSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets


def event_list(request):
    events = Event.objects.all().order_by('-date')
    events_dict = [{
        'name': event.name,
        'cover': event.images.filter(is_cover=True)[:1],
        'id': event.id
    } for event in events]
    return render(request, 'event.html', locals())


def event_detail(request, id):
    try:
        event = Event.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404

    return render(request, 'event_detail.html', locals())


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
