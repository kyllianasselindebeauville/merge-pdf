import argparse
import os
from typing import Optional, List

from PyPDF2 import PdfMerger

def merge_pdf(files: Optional[List[str]] = None,
              output: Optional[str] = None) -> bool:
    if files is None or not files:
        files = []
        for filename in os.listdir():
            if filename.endswith('.pdf'):
                files.append(filename)
        files.sort(key = str.lower)

    if len(files) > 1:
        merger = PdfMerger()

        for pdf in files:
            merger.append(pdf)

        if output is None or not output:
            output = f'{files[0][:-4]}-merged.pdf'
        else:
            if not output.endswith('.pdf'):
                output = f'{output}.pdf'

        merger.write(output)
        merger.close()
        return True
    else:
        return False


def main():
    parser = argparse.ArgumentParser(description='Merge PDF files.')

    parser.add_argument('files', nargs='*', type=str,
                        help='PDF files to merge')
    parser.add_argument('-o', '--output', type=str,
                        help='Name of the resulting pdf', metavar='file')

    args = parser.parse_args()
    merge_pdf(**vars(args))

if __name__ == '__main__':
    main()
