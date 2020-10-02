from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm


@login_required
def index(request):
    form = ProjectForm()
    context = {
        'form': form
    }
    return render(request, 'management/index.html', context)


@login_required
def create(request):
    form = ProjectForm()
    context = {
        'form': form
    }
    return render(request, 'management/create.html', context)
