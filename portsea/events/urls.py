from django.conf.urls import url
from events import views

app_name = 'events'
urlpatterns = [
    url(r'^event/$', views.events, name="events"),
]