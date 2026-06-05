from django.contrib import admin
from .models import Category, Tag, Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'is_featured', 'created_at')
    list_filter = ('status', 'category', 'is_featured')
    search_fields = ('title', 'blog_body', 'short_description')
    list_editable = ('is_featured',)
    prepopulated_fields = { 'slug' : ('title',)}



admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)
