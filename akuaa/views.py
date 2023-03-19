from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    news = LatestNews.objects.all()
    
    context = {
        'blogs':blogs,
        'news':news
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
        resume = request.FILES['resume']
        cover_letter = request.FILES['cover_letter']
        career = Career(name=fullname, email=email, phone=phone, position=position, location=location, linkedin=linkedin, portfolio=portfolio, choice1=choice1, choice2=choice2, resume=resume, cover_letter=cover_letter)
        career.save()
    
        
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
