from django.apps import AppConfig


class SmAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sm_app'

    def ready(self) -> None:
        import sm_app.signals
        