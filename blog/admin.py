from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Category, Tag, Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'is_featured', 'created_at')
    list_filter = ('status', 'category', 'is_featured')
    search_fields = ('title', 'blog_body', 'short_description')
    list_editable = ('is_featured',)
    prepopulated_fields = { 'slug' : ('title',)}

class BlogAdminForm(forms.ModelForm):
    blog_body = forms.CharField(
        widget=CKEditor5Widget(config_name='default')
    )

    class Meta:
        model = Blog
        fields = "__all__"


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_display = (
        "title",
        "category",
        "status",
        "is_featured",
        "created_at",
    )

    list_filter = (
        "status",
        "category",
        "is_featured",
    )

    search_fields = (
        "title",
        "short_description",
    )    



admin.site.register(Category)
admin.site.register(Tag)

