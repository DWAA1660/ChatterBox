"""
Default ChatterBox settings for Django.
"""
from django.conf import settings
from chatterbox import constants


ChatterBox_SETTINGS = getattr(settings, 'ChatterBox', {})

ChatterBox_DEFAULTS = {
    'name': 'ChatterBox',
    'storage_adapter': 'chatterbox.storage.DjangoStorageAdapter',
    'django_app_name': constants.DEFAULT_DJANGO_APP_NAME
}

ChatterBox = ChatterBox_DEFAULTS.copy()
ChatterBox.update(ChatterBox_SETTINGS)
