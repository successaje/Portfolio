from django.shortcuts import render
from .models import Project

def homePage(request):
    projects = Project.objects.all()
    return render(request, 'main/home.html', {'projects':projects})
