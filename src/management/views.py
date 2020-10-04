from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from main.models import Project


@login_required
def index(request):
    projects = Project.objects.all()
    context = {
        'posts': projects
    }
    return render(request, 'management/index.html', context)


@login_required
def create(request):
    form = ProjectForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        form = ProjectForm(request.POST or None, request.FILES or None)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/management/')

    context = {
        'form': form
    }
    return render(request, 'management/create.html', context)


@login_required
def delete(request, id):
    project = Project.objects.get(id=id)
    project.delete()

    return HttpResponseRedirect('/management/')


@login_required
def update(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(request.POST or None,
                       request.FILES or None, instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST or None,
                           request.FILES or None, instance=project)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/admin/')

    context = {
        'form': form
    }
    return render(request, 'management/update.html', context)
