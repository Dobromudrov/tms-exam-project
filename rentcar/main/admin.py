from django.contrib import admin
from .models import *


class CarsTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'is_published', 'photo', 'time_create', 'time_update')
    list_display_links = ('id', 'title', 'cat')
    search_fields = ('id', 'title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(CarsTable, CarsTableAdmin)
admin.site.register(Category, CategoryAdmin)


