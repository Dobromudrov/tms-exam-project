from django.contrib import admin
from .models import *


class CarsTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'is_published', 'price', 'photo', 'time_create', 'time_update', 'slug')
    list_display_links = ('id', 'title', 'cat')
    search_fields = ('id', 'title',)
    list_editable = ('is_published', 'price')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class OrderTableAdmin(admin.ModelAdmin):
    list_display = ('choice', 'phone_number', 'comment', 'time_create', 'author')


admin.site.register(CarsTable, CarsTableAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OrderTable, OrderTableAdmin)

