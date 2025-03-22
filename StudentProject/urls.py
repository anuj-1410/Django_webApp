"""
URL configuration for StudentProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from app1 import views as app1_views
from app2 import views as app2_views

urlpatterns = [
    path('', app1_views.home, name='home'),
    path('about/', app1_views.about, name='about'),
    path('services/', app1_views.services, name='services'),
    path('team/', app2_views.team, name='team'),
    path('contact/', app2_views.contact, name='contact'),
]

