"""portsea URL Configuration
"""

from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^', include('portal.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^events/', include('events.urls')),
]
