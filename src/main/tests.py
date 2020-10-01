from django.test import TestCase
from .models import Project


class ProjectTestCase(TestCase):
    def test_creation_of_projects(self):
        Project.objects.create(project_name='Test Website 1', project_description='This is website made through a test',
                               project_url='https://www.google.com', author='TestUser', author_email='lokotamathemastermind2@gmail.com', is_in_progress=True)
        print('Successfully created test project model object')
        projects = Project.objects.get(id=1)

        print('\nCreated Project', projects)

    def test_deletion_of_projects(self):
        Project.objects.create(project_name='Test Website 2', project_description='This is website made through a test',
                               project_url='https://www.google.com', author='TestUser', author_email='lokotamathemastermind2@gmail.com', is_in_progress=True)
        print('Successfully created test project model object')
        print(Project.objects.all())
        projects = Project.objects.get(project_name='Test Website 2')
        projects.delete()
        print('Successfully deleted test project model object')
        print(Project.objects.all())
