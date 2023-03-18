from django.db import models

CHOICES = (
    ("YES", "Yes"),
    ("No", "No"),
)

class Career(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField(null=False, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=False)
    position = models.TextField(null=True, blank=False)
    location = models.CharField(max_length=100)
    linkedin = models.URLField(null=True, blank=False)
    portfolio = models.URLField(null=True, blank=False)
    choice1 = models.CharField(max_length=3, choices=CHOICES, default="YES")
    choice2 = models.CharField(max_length=3, choices=CHOICES, default="YES")
    resume = models.FileField()
    cover_letter = models.FileField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    
    def __str__(self):
        return self.name