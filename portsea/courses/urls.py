from django.conf.urls import url
from courses  import views

app_name = 'courses'
urlpatterns = [
    url(r'^course/$', views.courses, name="courses"),
    url(r'^add_course/$', views.edit_course, name="add_course"),
    url(r'^edit_course/(?P<course_id>[0-9]+)/$', views.edit_course, name="edit_course"),
    url(r'^course_detail/(?P<course_id>[0-9]+)/$', views.course_detail, name="course_detail"),
    url(r'^course_detail/(?P<download_type>[\w]+)/(?P<paperwork_id>[0-9]+)/$', views.download_pdf, name="download_pdf"),
    url(r'^course_detail/show/(?P<paperwork_id>[0-9]+)/$', views.download_pdf, name="show_pdf"),
]