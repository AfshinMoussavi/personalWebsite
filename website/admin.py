from django.contrib import admin
from . import models

@admin.register(models.Contace)
class AdminContact(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['name', 'email', 'subject', 'created_date']
    list_filter = ['email']
    search_fields = ['name', 'message']