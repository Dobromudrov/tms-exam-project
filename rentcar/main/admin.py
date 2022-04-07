from django.contrib import admin
from .models import *


class CarsTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'is_published', 'photo', 'time_create', 'time_update', 'slug')
    list_display_links = ('id', 'title', 'cat')
    search_fields = ('id', 'title',)
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(CarsTable, CarsTableAdmin)
admin.site.register(Category, CategoryAdmin)


