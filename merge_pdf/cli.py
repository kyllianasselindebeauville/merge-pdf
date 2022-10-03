import argparse

from merge_pdf.version import __version__


def parse_args():
    """Parses arguments from the command-line.

    Creates a parser, adds arguments to the parser, parses those arguments.

    Returns:
        An argparse.Namespace object containing the arguments as attributes.
    """
    parser = argparse.ArgumentParser(prog='merge-pdf',
                                     description='Merge PDF files.')

    parser.add_argument('files', nargs='*', type=str,
                        help='PDF files to merge')
    parser.add_argument('-o', '--output', type=str,
                        help='name of the output file', metavar='out')
    parser.add_argument('-V', '--version', action='version',
                        version=f'%(prog)s {__version__}')

    args = parser.parse_args()
    return args
