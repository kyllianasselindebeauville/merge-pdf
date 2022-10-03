from merge_pdf.cli import parse_args
from merge_pdf.pdf import merge_pdf


def main():
    args = parse_args()
    merge_pdf(**vars(args))


if __name__ == '__main__':
    main()
