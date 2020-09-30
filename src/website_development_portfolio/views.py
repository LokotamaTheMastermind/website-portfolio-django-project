from django.shortcuts import render
from django.conf import settings
from main.models import Project
from .utils import read_file_content


def index(request):
    latest_projects = Project.objects.all().order_by('-posted_at')[:4]

    file_content = read_file_content(latest_projects)

    context = {
        'settings': settings.DEBUG,
        'posts': latest_projects,
        'extra_information': file_content
    }
    return render(request, 'landing/index.html', context)
