from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['title','author' , 'status', 'counted_view', 'published_date', 'created_date']
    list_filter = ['status']
    search_fields = ['title', 'content']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass