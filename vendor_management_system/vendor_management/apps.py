from django.apps import AppConfig


class VendorManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vendor_management'

    # This method is called when the app is ready to be used.
    def ready(self):
        from . import signals
