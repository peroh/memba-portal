from django.contrib import admin
from courses.models import Course, CourseType, PaperworkHistory

# Register your models here.

class CourseInlineAdmin(admin.TabularInline):
    model = Course.members.through
    verbose_name = "Registered Course"
    verbose_name_plural = "Registered Courses"

class PaperworkHistoryAdmin(admin.ModelAdmin):
    list_display = ('paperwork', 'course')

admin.site.register(Course)
admin.site.register(CourseType)
admin.site.register(PaperworkHistory, PaperworkHistoryAdmin)