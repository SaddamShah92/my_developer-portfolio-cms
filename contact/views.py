import logging
import resend

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from .forms import ContactForm


logger = logging.getLogger(__name__)

resend.api_key = settings.RESEND_API_KEY


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            logger.error("CONTACT STEP 1: form valid")

            inquiry = form.save()

            logger.error("CONTACT STEP 2: inquiry saved")

            resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": [settings.EMAIL_HOST_USER],
                "subject": f"New Portfolio Inquiry from {inquiry.name}",
                "text": f"""
Name: {inquiry.name}

Email: {inquiry.email}

Company: {inquiry.company}

Message:

{inquiry.message}
                """,
            })

            logger.error("CONTACT STEP 3: resend sent")

            messages.success(
                request,
                " &nbsp;&nbsp;&nbsp; Thank you for reaching out! Your message has been sent successfully. I'll review it and get back to you as soon as possible. 🙂"
            )

            return redirect('contact')

    else:
        form = ContactForm()

    return render(
        request,
        'contact/contact.html',
        {'form': form}
    )