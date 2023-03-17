from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'akuaa/home.html')


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'akuaa/about.html', context)

def service(request):
    context = {
        'title': 'Services',
    }
    return render(request, 'akuaa/service.html', context)

def foundation(request):
    context = {
        'title': 'Foundation',
    }
    return render(request, 'akuaa/foundation.html', context)
def career(request):
    context = {
        'title': 'Career',
    }
    return render(request, 'akuaa/career.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        return render(request, 'akuaa/contact.html')
    context = {
        'title': 'Contact',
    }
    return render(request, 'akuaa/contact.html', context)
