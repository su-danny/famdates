__author__ = 'vb'
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from account.models import EventJoin

def live_events(request, template_name='events/live_events.html'):

    ctx = {
        'events': Event.objects.filter(type__exact='pub'),
        'joined_events': [ej.event.id for ej in EventJoin.objects.all()]
    }

    return render(request, template_name, ctx)


def details(request, event_id, template_name='events/details.html'):
    event = get_object_or_404(Event, pk=event_id)
    ctx = {
        'event': event
    }
    return render(request, template_name, ctx)