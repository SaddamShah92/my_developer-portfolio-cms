from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=99)
    email = models.EmailField()
    company= models.CharField(max_length=150, blank = True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Contactmodel"

