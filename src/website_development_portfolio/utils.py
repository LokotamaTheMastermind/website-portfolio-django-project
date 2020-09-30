from django.conf import settings


def read_file_content(iterable):
    import os

    for project in iterable:
        PHYSICAL_PATH = f"{os.path.join(os.path.dirname(settings.BASE_DIR), 'cdn')}/{project.extra_information.url}".replace(
            '//', '/').replace('\\', '/')
        with open(f"{PHYSICAL_PATH}") as extra_info_file:
            content = extra_info_file.readlines()
            for i in content:
                line = i.strip()
                return line
