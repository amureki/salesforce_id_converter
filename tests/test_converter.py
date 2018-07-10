from unittest import TestCase

from salesforce_id_converter.converter import Converter, get_bit

SALESFORCE_SHORT_ID = '00558000001N0Ke'
SALESFORCE_LONG_ID = '00558000001N0KeAAK'


class TestConverter(TestCase):
    def test_get_bit(self):
        bit_mapping = [
            ('A', '1'),
            ('Z', '1'),
            ('a', '0'),
            ('z', '0'),
            (1, '0'),
            (999, '0'),
        ]

        for char, mapped in bit_mapping:
            assert get_bit(char) == mapped

    def test_convert(self):
        converter = Converter(short=SALESFORCE_SHORT_ID)
        assert converter.convert() == SALESFORCE_LONG_ID
