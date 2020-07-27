from django.apps import AppConfig


class AppacountsConfig(AppConfig):
    name = 'appacounts'

    def ready(self):
        import appacounts.signals
