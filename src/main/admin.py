from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_description', 'project_picture', 'project_url', 'author',
                    'posted_at', 'is_in_progress', 'author_email']
    list_filter = ['project_name', 'project_description', 'author',
                   'posted_at', 'is_in_progress', 'author_email']
    search_fields = ['author', 'author_email', 'project_name']


admin.site.register(Project, ProjectAdmin)
