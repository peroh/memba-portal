from django.contrib import admin
from events.models import Event, EventType

class EventInlineAdmin(admin.TabularInline):
    model = Event.member_signup.through

class EventAdmin(admin.ModelAdmin):
    inlines = (EventInlineAdmin,)

admin.site.register(Event, EventAdmin)
admin.site.register(EventType)
