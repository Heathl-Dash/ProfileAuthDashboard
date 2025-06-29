from django.apps import AppConfig


class ProfilecoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profileCore'

    def ready(self):
        from profileCore import signals