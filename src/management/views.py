from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from main.models import Project
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


@login_required
def index(request):
    project_list = Project.objects.all().order_by('-posted_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(project_list, 4)

    number_of_results = paginator.count

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    if not project_list:
        empty = True
    elif project_list:
        empty = False

    context = {
        'posts': projects,
        'num_of_results': number_of_results,
        'empty': empty
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
            return HttpResponseRedirect('/management/')

    context = {
        'form': form
    }
    return render(request, 'management/update.html', context)
