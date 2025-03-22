from django.urls import path
from . import views

urlpatterns = [
    path('', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
]