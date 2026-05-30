from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):

    class Meta:

        model = ContactModel

        fields = [
            'name',
            'email',
            'company',
            'message'
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Name'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Email'
                }
            ),

            'company': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Company Name (Optional)'
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Tell me about your project...',
                    'rows': 3
                }
            ),
        }
        