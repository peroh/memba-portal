from django.contrib import admin
from members.models import Member
from awards.admin import AwardInlineAdmin
from courses.admin import CourseInlineAdmin



class MemberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_of_birth','club',)
    inlines = (AwardInlineAdmin, CourseInlineAdmin)

admin.site.register(Member, MemberAdmin)