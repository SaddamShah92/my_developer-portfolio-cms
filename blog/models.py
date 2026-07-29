from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(unique=True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = 'Categories' 

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 50)
   

    def __str__(self):
        return self.name
    
STATUS_CHOICES = (
    ( 'draft' , 'Draft'), 
    ('published', 'Published'),
)


class Blog(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(unique = True, blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    featured_image = models.ImageField(upload_to = 'blog/uploads/%Y/%m/%d', null = True, blank = True)
    short_description = models.TextField(max_length = 500)
    blog_body = CKEditor5Field('Blog Content',config_name='default')
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'draft')
    tags = models.ManyToManyField(Tag, blank = True)
    is_featured = models.BooleanField(default = False) 
    reading_time = models.PositiveIntegerField(default=5) 
    seo_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta: 
        ordering = ['-created_at']

    def __str__(self):
        return self.title

