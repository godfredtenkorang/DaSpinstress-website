from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog-img', default='')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        if img.height > 350 or img.width > 350:
            output_size = (350, 350)
            img.thumbnail(output_size)
            img.save(self.image.path)

CHOICES = (
    ("YES", "Yes"),
    ("No", "No"),
)

class LatestNews(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="LatestNews-img")
    date = models.DateTimeField(default=timezone.now)
    link = models.URLField()
    
    def __str__(self):
        return self.title

class Career(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    position = models.TextField()
    location = models.CharField(max_length=100)
    linkedin = models.URLField()
    portfolio = models.URLField()
    choice1 = models.CharField(max_length=3, choices=CHOICES, default="YES")
    choice2 = models.CharField(max_length=3, choices=CHOICES, default="YES")
    resume = models.FileField(upload_to='resume-file')
    cover_letter = models.FileField(upload_to='cover_letter-file')
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    
    def __str__(self):
        return self.name


    
class DJService(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='dj-img', default='')
    position = models.CharField(max_length=100)
    content1 = models.TextField()
    address = models.CharField(max_length=100)
    content2 = models.TextField()
    twitter = models.URLField()
    facebook = models.URLField()
    linkedin = models.URLField()
    instagram = models.URLField()
    youtube = models.URLField()
    
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    event = models.CharField(max_length=100)
    event_date = models.CharField(max_length=10)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.fullname