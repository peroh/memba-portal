from django.conf.urls import url

from courses import views

app_name = 'courses'
urlpatterns = [

    # new class-based views

    url(r'^course_list/$', views.CourseListAll.as_view(), name="courses"),
    url(r'^course_list/([\w-]+)/$', views.CourseListFilter.as_view()),
    url(r'^course_detail/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view(), name="course_detail"),
    url(r'^add_course/$', views.AddCourse.as_view(), name="add_course"),
    url(r'^update_course/(?P<pk>[0-9]+)/$', views.CourseUpdate.as_view(), name="update_course"),
    url(r'^course_detail/(?P<pk>[0-9]+)/members/$', views.CourseMembers.as_view(), name="course_members"),

    # current function-based views

    url(r'^course_detail/(?P<course_id>[0-9]+)/members/add_member/$', views.add_course_members, name="add_course_members"),
    url(r'^course_detail/(?P<download_type>[\w]+)/(?P<paperwork_id>[0-9]+)/$', views.download_pdf, name="download_pdf"),
    url(r'^course_detail/show/(?P<paperwork_id>[0-9]+)/$', views.download_pdf, name="show_pdf"),
    url(r'^course_detail/(?P<course_id>[0-9]+)/add_paperwork/(?P<paperwork_id>[0-9]+)/$', views.create_paperwork, name="create_paperwork"),

    # old function-based views

    # url(r'^course/$', views.courses, name="courses"),
    # url(r'^course_detail/(?P<course_id>[0-9]+)/$', views.course_detail, name="course_detail"),
    # url(r'^add_course/$', views.add_course, name="add_course"),
    # url(r'^edit_course/(?P<course_id>[0-9]+)/$', views.edit_course, name="edit_course"),
    # url(r'^course_detail/(?P<course_id>[0-9]+)/members/$', views.course_members, name="course_members"),

]
