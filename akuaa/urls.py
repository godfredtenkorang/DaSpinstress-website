from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('client/', views.client, name='client'),
    path('foundation/', views.foundation, name='foundation'),
    path('career/', views.career, name='career'),
    path('contact/', views.contact, name='contact'),
    path('book/<int:book>/', views.book, name='book'),
]