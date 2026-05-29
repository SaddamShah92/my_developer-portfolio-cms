from django.db import models

class ContactForm(models.Model):
    PROJECT_CHOICES = [
        ('django', 'Django Development'),
        ('api', 'API Development'),
        ('automation', 'Business Automation'),
        ('consulting', 'Consulting'),
        ('other', 'Other'),
    ]

    BUDGET_CHOICES = [
        ('under_500', 'Under $500'),
        ('500_1000', '$500 - $1000'),
        ('1000_5000', '$1000 - $5000'),
        ('5000_plus', '$5000+'),
        ('custom', 'Custom'),
    ]

    name = models.CharField(max_length=99)
    email = models.EmailField()
    company= models.CharField(max_length=150, blank = True)
    project_type = models.CharField(max_length=50, choices = PROJECT_CHOICES)
    budget = models.CharField(max_length = 20, choices = BUDGET_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.name} - {self.project_type}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "ContactForm"

