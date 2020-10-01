from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings


# Website Project model
class Project(models.Model):
    project_name = models.CharField(max_length=50, blank=False, null=False,
                                    help_text='Name of the website project', verbose_name='Project name', default='Example Site', unique=True)
    project_description = models.TextField(blank=False, null=False, verbose_name='Project description',
                                           help_text='Make this section long explaining what the project is about', default='This is a website I made for ...')
    project_picture = models.ImageField(blank=False, default='shared/pics/projects/default.jpg', null=False,
                                        help_text='Home page view of the project <em>Should be personal pictures and not from external sites</em><br>It must be one picture', verbose_name='Project picture path', upload_to='pics/projects')
    project_url = models.URLField(blank=False, null=False, default='https://github.com/LokotamaTheMastermind/',
                                  help_text='GitHub link to project for personal account', verbose_name='Source code link')
    author = models.CharField(max_length=50, blank=False, null=False,
                              help_text='Author of the project', verbose_name='Project author', default='LokotamaTheMastermind')
    author_email = models.EmailField(help_text='Email of the project owner', verbose_name='Owner email',
                                     blank=False, null=False, default='lokotamathemastermind2@gmail.com')
    posted_at = models.DateTimeField(
        auto_now_add=True, help_text='Different from project creation date', verbose_name='Post date', blank=False, null=False)
    extra_information = models.FileField(
        help_text='Extra information about project', blank=False, null=False, upload_to='info/', verbose_name='Extra information file path', validators=[FileExtensionValidator([
            'txt'
        ])], default='shared/info/default.txt')
    is_in_progress = models.BooleanField(default=False, blank=False, null=False,
                                         verbose_name='Project status', help_text='Are you done with the project')

    def __str__(self) -> str:
        return self.project_name

    def read_file_content(self):
        import os

        PHYSICAL_PATH = f"{os.path.join(os.path.dirname(settings.BASE_DIR), 'cdn')}/{self.extra_information.url}".replace(
            '//', '/').replace('\\', '/')
        with open(f"{PHYSICAL_PATH}") as extra_info_file:
            content = extra_info_file.readlines()
            for i in content:
                line = i.strip()
                return line
