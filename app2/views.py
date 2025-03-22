from django.shortcuts import render

def team(request):
    return render(request, 'team.html')

def contact(request):
    return render(request, 'contact.html')