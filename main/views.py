from django.shortcuts import render
from .models import Project, Skill

def homePage(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')
    context = {'projects':projects, 'skills':skills, 'detailedSkills':detailedSkills}
    return render(request, 'main/home.html', context)


def projectPage(request, pk):
    context = {}
    return(request, 'main/project.html', context)
