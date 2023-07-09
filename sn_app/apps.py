from django.apps import AppConfig


class SnAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sn_app'

    def ready(self) -> None:
        import sn_app.signals