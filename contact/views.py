import resend

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from .forms import ContactForm


resend.api_key = settings.RESEND_API_KEY


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            inquiry = form.save()

            resend.Emails.send({
                "from": "Portfolio Contact <contact@saddamshah.com>",
                "to": [settings.CONTACT_EMAIL],
                "subject": f"New Portfolio Inquiry from {inquiry.name}",
                "text": f"""
Name: {inquiry.name}

Email: {inquiry.email}

Company: {inquiry.company}

Message:

{inquiry.message}
                """,
            })

            messages.success(
                request,
                " &nbsp;&nbsp;&nbsp; Thank you for reaching out! Your message has been sent successfully. I'll review it and get back to you as soon as possible. 🙂"
            )

            return redirect('contact')

    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)