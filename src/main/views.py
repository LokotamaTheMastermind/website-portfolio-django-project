from django.shortcuts import render
from .models import Project
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from website_development_portfolio.utils import read_file_content


def projects(request):
    project_list = Project.objects.all().order_by('-posted_at')
    page = request.GET.get('page', 1)

    paginator = Paginator(project_list, 4)
    number_of_results = paginator.count

    file_content = read_file_content(project_list)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    context = {
        'projects': projects,
        'num_of_results': number_of_results,
        'extra_information': file_content
    }
    return render(request, 'main/index.html', context)
