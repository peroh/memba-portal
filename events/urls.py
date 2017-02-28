from django.conf.urls import url
from events import views

app_name = 'events'
urlpatterns = [
    url(r'^event/$', views.events, name="events"),
    url(r'^add_event/$', views.add_event, name="add_event"),
    url(r'^edit_event/(?P<event_id>[0-9]+)/$', views.edit_event, name="edit_event"),
    url(r'^event_detail/(?P<event_id>[0-9]+)/$', views.event_detail, name="event_detail"),
    url(r'^event_detail/(?P<event_id>[0-9]+)/members/$', views.event_members, name="event_members"),
    url(r'^event_detail/(?P<event_id>[0-9]+)/members/add_member$', views.add_event_members, name="add_event_members")

]