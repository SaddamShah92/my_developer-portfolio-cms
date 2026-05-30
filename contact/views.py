from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    form = ContactForm()
    

    context = {
        'form' : form,  
    }

    return render(request, 'contact/contact.html', context)


