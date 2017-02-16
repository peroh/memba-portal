from django.shortcuts import render
from events.models import Event

def events(request):
    event_list = Event.objects.all()
    context_dict = {'event_list': event_list}
    return render(request, 'events/events.html', context_dict)
