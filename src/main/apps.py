from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    verbose_name = 'Root Application'

    def ready(self):
        import main.signals
