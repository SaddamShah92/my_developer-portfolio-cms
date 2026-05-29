from django.contrib import admin
from .models import ContactForm

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'project_type',
        'budget',
        'created_at'
    )

    list_filter = (
        'project_type',
        'budget',
        'created_at'
    )

    search_fields = (
        'name',
        'email',
        'company'
    )