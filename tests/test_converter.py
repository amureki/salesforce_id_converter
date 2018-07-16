from unittest import TestCase

from salesforce_id_converter.converter import Converter, get_bit


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
        salesforce_test_ids = (
            ('001A0000006Vm9u', '001A0000006Vm9uIAC'),
            ('00558000001N0Ke', '00558000001N0KeAAK'),
            ('00D0Q0000008aI9', '00D0Q0000008aI9UAI'),
            ('0016E00000YbJrD', '0016E00000YbJrDQAV'),
        )
        for short_id, long_id in salesforce_test_ids:
            converter = Converter(short=short_id)
            assert converter.convert() == long_id
