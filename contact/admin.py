from django.contrib import admin
from .models import ContactModel

@admin.register(ContactModel)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = (
    'name',
    'email',
    'company',
    'created_at'
)

    search_fields = (
        'name',
        'email',
        'company'
    )