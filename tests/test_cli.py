from unittest import TestCase

from salesforce_id_converter.cli import main as sfc_main


class TestMain(TestCase):
    def test_main(self):
        self.assertEqual(sfc_main([None]), 0)
