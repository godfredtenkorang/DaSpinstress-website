from django.shortcuts import render, redirect
from .models import *
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

# Create your views here.
def home(request):
    blogs = Blog.objects.order_by('-date_posted')
    clients = HomeClient.objects.order_by('-date')
    
    context = {
        'blogs':blogs,
        'clients':clients
    }
    return render(request, 'akuaa/home.html', context)


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

def client(request):
    clients = Client.objects.all()
    context = {
        'title': 'Clients',
        'clients': clients
    }
    return render(request, 'akuaa/clients.html', context)

def foundation(request):
    context = {
        'title': 'Foundation',
    }
    return render(request, 'akuaa/foundation.html', context)
def career(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        position = request.POST['position']
        location = request.POST['location']
        linkedin = request.POST['linkedin']
        portfolio = request.POST['portfolio']
        choice1 = request.POST['choice1']
        choice2 = request.POST['choice2']
        try:
            resume = request.FILES['resume']
        except MultiValueDictKeyError:
            resume = False
        try:
            cover_letter = request.FILES['cover_letter']
        except MultiValueDictKeyError:
            cover_letter = False
        career = Career(name=fullname, email=email, phone=phone, position=position, location=location, linkedin=linkedin, portfolio=portfolio, choice1=choice1, choice2=choice2, resume=resume, cover_letter=cover_letter)
        career.save()
        messages.success(request, "Your forms has been submitted, you will here from us very soon")
        return redirect('career')
        
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
        messages.success(request, "Your forms has been submitted, you will here from us very soon")
        return render(request, 'akuaa/contact.html')
    context = {
        'title': 'Contact',
    }
    return render(request, 'akuaa/contact.html', context)


def book(request, book):
    books = Client.objects.get(pk=book)
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        event = request.POST['event']
        event_date = request.POST['event_date']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        location = request.POST['location']
        message = request.POST['message']
        booking = Book(fullname=fullname, email=email, phone=phone, event=event, event_date=event_date, start_time=start_time, end_time=end_time, location=location, message=message)
        booking.save()
        messages.success(request, "Your booking form has been submitted, you will hear from us very soon!")
    context = {
        'books':books,
    }
    return render(request, 'akuaa/book.html', context)