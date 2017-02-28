from django.shortcuts import render, HttpResponseRedirect, reverse

from events.forms import EventForm, AddEventMembers
from events.models import Event, EventSignup
from members.models import Member


def events(request):
    event_list = Event.objects.all()

    context_dict = {'event_list': event_list}
    return render(request, 'events/events.html', context_dict)


def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)

    context_dict = {
        'event': event,
    }
    return render(request, 'events/event_detail.html', context_dict)


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('events:events'))
        else:
            print form.errors
    else:
        form = EventForm()

    context_dict = {
        'form': form,
    }
    return render(request, 'events/event_add.html', context=context_dict)


def edit_event(request, event_id):
    if event_id:
        event = Event.objects.get(pk=event_id)
    else:
        event = None

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid:
            form.save(commit=True)
            if event_id:
                return HttpResponseRedirect(reverse('events:event_detail', kwargs={'event_id': event_id}))
            else:
                return HttpResponseRedirect(reverse('events:events'))
        else:
            print form.errors
    else:
        form = EventForm(instance=event)

    context_dict_edit = {
        'form': form,
        'event': event,
    }
    context_dict_add = {
        'form': form,
    }

    if event_id:
        return render(request, 'events/event_edit.html', context=context_dict_edit)
    else:
        return render(request, 'events/event_add.html', context=context_dict_add)


def event_members(request, event_id):
    event = Event.objects.get(pk=event_id)
    member_list = event.member_signup.all()
    context_dict = {
        'member_list': member_list,
        'event': event
    }
    return render(request, 'events/event_members.html', context_dict)

def add_event_members(request, event_id):

    event = Event.objects.get(pk=event_id)
    form = AddEventMembers(event_id=event_id)
    members_not_registered = Member.objects.exclude(id__in=(Event.objects.get(id=event_id).member_signup.all()))

    if request.method == 'POST':
        form = AddEventMembers(request.POST, event_id=event_id)
        if form.is_valid():
            new_members = form.cleaned_data['members']
            for member in new_members:
                EventSignup.objects.create(member=member, event=event)
            return HttpResponseRedirect(reverse('events:event_members', kwargs={'event_id':event.id}))
        else:
            print form.errors

    context_dict = {
        'event': event,
        'form': form,
        'members_not_registered': members_not_registered,
    }

    return render(request, 'events/add_event_members.html', context_dict)