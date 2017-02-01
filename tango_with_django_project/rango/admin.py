from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {'fields': ['title']}),
    #     ('Category', {'fields': ['category']}),
    #     ('URL', {'fields': ['url']}),
    #     ('Views', {'fields': ['views']}),
    # ]

    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'likes', 'views')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
