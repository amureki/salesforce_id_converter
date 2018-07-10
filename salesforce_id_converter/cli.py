from argparse import ArgumentParser

from salesforce_id_converter.converter import Converter
from salesforce_id_converter.utils import copy_to_clipboard

COLOR_GREEN = '\033[92m'
COLOR_DEFAULT = '\033[0m'

parser = ArgumentParser(
    prog='sfc',
    description='Convert 15 character Salesforce id into a 18 character id'
)
parser.add_argument('id', help='15 character id to convert')


def main(cli_args=None):
    if cli_args is not None:
        known_args = parser.parse_args(cli_args)
    else:
        known_args = parser.parse_args()

    if not known_args.id:
        parser.print_usage()
        return 0

    short_id = known_args.id

    converter = Converter(short=short_id)
    long_id = converter.convert()
    msg = 'You converted 15 character `{}` into 18 character: \n{}{}'.format(
        short_id,
        COLOR_GREEN,
        long_id
    )
    print(msg)
    copy_to_clipboard(long_id)
    print('{}New id has been copied to your clipboard'.format(COLOR_DEFAULT))
    return 0


if __name__ == '__main__':
    exit(main())
