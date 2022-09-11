from django.test import TestCase
from django.conf import settings


class SettingsTestCase(TestCase):

    def test_modified_settings(self):
        with self.settings(ChatterBox={'name': 'Jim'}):
            self.assertIn('name', settings.ChatterBox)
            self.assertEqual('Jim', settings.ChatterBox['name'])

    def test_name_setting(self):
        with self.settings():
            self.assertIn('name', settings.ChatterBox)
            self.assertEqual('Test Django ChatterBox', settings.ChatterBox['name'])
