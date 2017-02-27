from django.contrib import admin
from members.models import Member
from awards.admin import AwardInlineAdmin
from courses.admin import CourseInlineAdmin
from events.admin import EventInlineAdmin

class MemberInlineAdmin(admin.TabularInline):
    model = Member

    verbose_name = 'Member Details'
    verbose_name_plural = 'Member Details'

class MemberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_of_birth','club',)
    inlines = (AwardInlineAdmin, CourseInlineAdmin, EventInlineAdmin)

admin.site.register(Member, MemberAdmin)