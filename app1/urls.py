from django.urls import path
from .views import home, about, services, team, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('team/', team, name='team'),
    path('contact/', contact, name='contact'),
]
