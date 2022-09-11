from unittest import TestCase
from chatterbox import __main__ as main


class CommandLineInterfaceTests(TestCase):
    """
    Tests for the command line tools that are included with ChatterBox.
    """

    def test_get_chatterbox_version(self):
        version = main.get_chatterbox_version()
        version_parts = version.split('.')
        self.assertEqual(len(version_parts), 3)
        self.assertTrue(version_parts[0].isdigit())
        self.assertTrue(version_parts[1].isdigit())
