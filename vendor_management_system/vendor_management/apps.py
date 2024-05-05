from django.apps import AppConfig


class VendorManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vendor_management'

    def ready(self):
        """
        Method called when the application is ready.
        Imports the signals module to register the signals.
        """
        from . import signals
