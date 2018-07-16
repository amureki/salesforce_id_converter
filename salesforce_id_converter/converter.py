import string


def get_bit(char) -> str:
    return '1' if str(char).isupper() else '0'


class Converter:
    """
    Convert 15 character Salesforce id into a 18 character id.

    Algorithm is explained here:
    http://salesforce.stackexchange.com/questions/1653/what-are-salesforce-ids-composed-of
    """

    def __init__(self, short):
        self.short = short

    def _convert_chunk_to_bit(self, chunk):
        binary_repr = ''.join(reversed([get_bit(char) for char in chunk]))
        return str(int(binary_repr, 2))

    def convert(self):
        suffix = ''
        # split id into three chunks
        chunks = [self.short[i:i+5] for i in range(0, len(self.short), 5)]
        # construct an array of A-Z and 0-5
        array = string.ascii_uppercase + string.digits[:6]

        for chunk in chunks:
            bit_char = self._convert_chunk_to_bit(chunk)
            suffix += array[int(bit_char)]

        return self.short + suffix
