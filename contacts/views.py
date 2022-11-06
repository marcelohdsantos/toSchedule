from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.http import Http404


def index(request):
    contacts = Contact.objects.all()

    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })

def see_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contacts/see_contact.html', {
        'contact': contact
    })
