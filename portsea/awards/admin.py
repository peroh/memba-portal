from django.contrib import admin
from awards.models import Award, Awarded

class AwardInlineAdmin(admin.TabularInline):
    model = Award.members.through

class AwardAdmin(admin.ModelAdmin):
    inlines = (AwardInlineAdmin,)

admin.site.register(Award, AwardAdmin)
