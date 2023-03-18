from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.http import Http404
from django.core.paginator import Paginator


def index(request):
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 25)

    page = request.GET.get('p')
    contacts = paginator.get_page(page)

    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })

def see_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contacts/see_contact.html', {
        'contact': contact
    })
