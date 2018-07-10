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

    def convert(self):
        suffix = ''
        chunks = [self.short[i:i+5] for i in range(0, len(self.short), 5)]
        array = string.ascii_uppercase + string.digits[:6]

        for chunk in chunks:
            bits = str(int(''.join([get_bit(char) for char in chunk]), 2))
            suffix += array[int(bits)]

        return self.short + suffix
