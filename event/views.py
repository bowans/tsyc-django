from django.http import HttpResponse, Http404
from django.shortcuts import render
from event.models import Event
from django.core.exceptions import ObjectDoesNotExist


def event_list(request):
    events = Event.objects.all().order_by('-date')
    events_dict = [{'name': event.name, 'cover': event.images.filter(is_cover=True)[:1], 'id': event.id} for event in events]
    return render(request, 'event.html', locals())


def event_detail(request, id):
    try:
        event = Event.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404

    return render(request, 'event_detail.html', locals())
