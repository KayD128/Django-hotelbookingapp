from email import message
from tkinter import PhotoImage
from django.shortcuts import render
from hotelbooking.customerapp.forms import Contact_form
from .models import Contact
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.core.mail import send_mail

# Create your views here.

def contact_us(request):
    if request.method == 'POST':
        contact_form = Contact_form(request.POST)
        if contact_form.is_valid():
            myName = contact_form.cleaned_data['name']
            myMail = contact_form.cleaned_data['mail']
            myNumber = contact_form.cleaned_data['phone']
            myMessage = contact_form.cleaned_data['message']

            my_message = Contact(name=myName, mail=myMail, phone=myNumber, message=myMessage)
            my_message.save()

            send_mail(
                myName,
                myMessage,
                myMail,
                ['ogunleyekolade25@gmail.com']    
            )

            messages.success(request, ('We have received your message and we will respond shortly. Thank you.'))
            return HttpResponsePermanentRedirect(reverse('contact'))
        else:
            messages.error(request, ("Please input the right contents."))
            return HttpResponsePermanentRedirect(reverse('contact'))
    else:
        contact_form = Contact_form()
    return render(request, 'customerapp/contact.html', {'contact_form': contact_form})


