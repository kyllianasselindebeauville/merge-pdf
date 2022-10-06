import os
from typing import Optional, List

from PyPDF2 import PdfMerger


def _get_pdf_files(files: Optional[List[str]] = None) -> List[str]:
    """Fetches existing pdf files from the provided files.

    Retrieves existing pdf files from the provided files or from the current
    directory.

    Args:
        files: A list of filenames.

    Returns:
        A list of existing pdf filenames.
    """
    pdf_files = []

    if files:
        for filename in files:
            if filename.endswith('.pdf'):
                pdf_files.append(filename)
            elif os.path.exists(f'{filename}.pdf'):
                pdf_files.append(f'{filename}.pdf')
    else:
        for filename in os.listdir():
            if filename.endswith('.pdf'):
                pdf_files.append(filename)
        pdf_files.sort(key=str.lower)

    return pdf_files


def _get_output_filename(pdf_files: List[str],
                         output: Optional[str] = None) -> str:
    """Generates the output filename.

    Generates a name for the output file according to the provided name if
    there is one or the name of the first file with '-merged' at the end.

    Args:
        pdf_files: A list of pdf filenames.
        output: Expected output filename.

    Returns:
        The correct output filename as a str.
    """
    if output:
        if not output.endswith('.pdf'):
            output = f'{output}.pdf'
    else:
        output = f'{pdf_files[0][:-4]}-merged.pdf'

    return output


def merge_pdf(files: Optional[List[str]] = None,
              output: Optional[str] = None) -> bool:
    """Merges pdf files into one output file.

    Merges pdf files using the PyPDF2 module.

    Args:
        files:
            A list containing the files to be merged.
            [default: files in the current directory]
        output:
            Name of the output file.
            [default: name of the first file with '-merged' at the end]

    Returns:
        A boolean indicating whether the files have been merged.
    """
    pdf_files = _get_pdf_files(files)

    if len(pdf_files) > 1:
        merger = PdfMerger()
        output_filename = _get_output_filename(pdf_files, output)

        for pdf in pdf_files:
            merger.append(pdf)

        with open(output_filename, 'wb') as output_file:
            merger.write(output_file)

        merger.close()
        return True
    else:
        return False


merge = merge_pdf
