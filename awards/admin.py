from django.contrib import admin
from awards.models import Award, Awarded

class AwardInlineAdmin(admin.TabularInline):
    model = Award.members.through

    verbose_name = "Award"
    verbose_name_plural = "Awards"

class AwardAdmin(admin.ModelAdmin):
    inlines = (AwardInlineAdmin,)

admin.site.register(Award, AwardAdmin)
