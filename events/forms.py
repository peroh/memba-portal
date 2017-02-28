from django import forms
from django.forms.extras.widgets import SelectDateWidget

from events.models import Event, EventType
from members.models import Member


class EventForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    type = forms.ModelChoiceField(queryset=EventType.objects.all())
    date = forms.DateField(required=False,
                           widget=SelectDateWidget(empty_label="---"))
    start_time = forms.TimeField(required=False)
    end_time = forms.TimeField(required=False)

    class Meta:
        model = Event
        fields = ['name', 'type', "date", "start_time", "end_time"]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Name of Event"
        self.fields['type'].label = "Type of Event"
        self.fields['date'].label = "Date"
        self.fields['start_time'].label = "Start Time"
        self.fields['end_time'].label = "End Time"


class AddEventMembers(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ['name', 'member_signup', 'date',
                   'start_time', 'end_time', 'type']

    def __init__(self, *args, **kwargs):
        event_id = kwargs.pop('event_id')
        # get members registered to event
        members_registered = Event.objects.get(id=event_id).member_signup.all()
        # list of all members not registered to event
        members_not_registered = Member.objects.exclude(
            id__in=members_registered
        )
        super(AddEventMembers, self).__init__(*args, **kwargs)
        self.fields['members'] = forms.ModelMultipleChoiceField(
            queryset=members_not_registered,
            widget=forms.CheckboxSelectMultiple
        )
