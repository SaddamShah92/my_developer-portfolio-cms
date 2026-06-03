from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True)

    class Meta:
        verbose_name_plural = 'Categories' 

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    pass
