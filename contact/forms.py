from django import forms
from .models import ContactForm


class ContactForm(forms.ModelForm):

    class Meta:

        model = ContactForm

        fields = [
            'name',
            'email',
            'company',
            'project_type',
            'budget',
            'message'
        ]

        widgets = {
            'message': forms.Textarea(
                attrs={
                    'rows': 6
                }
            )
        }