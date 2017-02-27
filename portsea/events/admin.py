from django.contrib import admin
from events.models import Event, EventType

class EventInlineAdmin(admin.TabularInline):
    model = Event.member_signup.through

    verbose_name = 'Event Signup'
    verbose_name_plural = 'Event Signups'

class EventAdmin(admin.ModelAdmin):
    inlines = (EventInlineAdmin,)

admin.site.register(Event, EventAdmin)
admin.site.register(EventType)
