from django.conf.urls import url
from members import views

app_name = 'members'
urlpatterns = [
    url(r'^members/$', views.members, name="members"),
    url(r'^add_member/$', views.add_member, name="add_member"),
    url(r'^add_member_success/$', views.add_member_success, name="add_member_success"),
]
