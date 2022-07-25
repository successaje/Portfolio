from django.shortcuts import render, redirect

from .models import Project, Skill
from .forms import ProjectForm

def homePage(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')
    context = {'projects':projects, 'skills':skills, 'detailedSkills':detailedSkills}
    return render(request, 'main/home.html', context)


def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'main/project.html', context)


def addProject(request):
    forms = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"forms":forms}
    return render(request, 'main/project_form.html', context)

def editProject(request, pk):
    project = Project.objects.get(id=pk)
    forms = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"forms":forms}
    return render(request, 'main/project_form.html', context)
