from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            inquiry = form.save()

            send_mail(
                subject=f"New Portfolio Inquiry from {inquiry.name}",

                message=f"""
Name: {inquiry.name}

Email: {inquiry.email}

Company: {inquiry.company}

Message:

{inquiry.message}
                """,

                from_email=settings.DEFAULT_FROM_EMAIL,

                recipient_list=[
                    settings.EMAIL_HOST_USER
                ],

                fail_silently=False
            )

            messages.success(
                request,
                " &nbsp;&nbsp;&nbsp; Thank you for reaching out! Your message has been sent successfully. I'll review it and get back to you as soon as possible. 🙂"
            )

            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'form' : form,  
    }

    return render(request, 'contact/contact.html', context)


