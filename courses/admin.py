from django.contrib import admin

from courses.models import Course, CourseType, PaperworkHistory, PaperworkTemplates


class CourseInlineAdmin(admin.TabularInline):
    model = Course.members.through
    verbose_name = "Registered Course"
    verbose_name_plural = "Registered Courses"


class PaperworkTemplatesInlineAdmin(admin.TabularInline):
    model = PaperworkTemplates


class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ('course_type', 'get_paperwork')
    inlines = (PaperworkTemplatesInlineAdmin,)


class PaperworkHistoryAdmin(admin.ModelAdmin):
    list_display = ('paperwork', 'course',)


class PaperworkTemplatesAdmin(admin.ModelAdmin):
    list_display = ('paperwork', 'course',)

admin.site.register(Course)
admin.site.register(CourseType, CourseTypeAdmin)
admin.site.register(PaperworkTemplates)
admin.site.register(PaperworkHistory, PaperworkHistoryAdmin)
