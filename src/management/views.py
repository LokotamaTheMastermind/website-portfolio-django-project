from django.shortcuts import render
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

    context = {
        'form': form
    }
    return render(request, 'management/create.html', context)


def delete(request, id):
    deleted = False
    project_id = Project.objects.get(id=id)

    if request.method == "POST":
        project_id.delete()
        deleted = True

    context = {
        'deleted': deleted,
        'item': project_id
    }
    return render(request, 'management/delete.html', context)


def update(request, id):
    context = {}
