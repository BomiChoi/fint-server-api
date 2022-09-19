import os

from django.apps import AppConfig


class CommonConfig(AppConfig):
    name = 'apps.common'

    def ready(self):
        import updater
        if not os.environ.get('APP'):
            os.environ['APP'] = 'True'
            updater.start()
