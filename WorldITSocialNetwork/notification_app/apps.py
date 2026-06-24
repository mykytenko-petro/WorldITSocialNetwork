from django.apps import AppConfig


class NotificationAppConfig(AppConfig):
    name = 'notification_app'

    def ready(self) -> None:
        from . import signals
