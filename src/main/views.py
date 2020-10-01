from django.shortcuts import render
from .models import Project
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


def projects(request):
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
        'projects': projects,
        'num_of_results': number_of_results,
        'empty': empty
    }
    return render(request, 'main/index.html', context)
