import argparse


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
                        help='Name of the resulting pdf', metavar='file')

    args = parser.parse_args()
    return args
