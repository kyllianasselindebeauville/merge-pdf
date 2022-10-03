import os
from typing import Optional, List

from PyPDF2 import PdfMerger


def _get_pdf_files(files: Optional[List[str]] = None) -> List[str]:
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


def _get_output_filename(pdf_files: List[str], output: Optional[str]) -> str:
    if output:
        if not output.endswith('.pdf'):
            output = f'{output}.pdf'
    else:
        output = f'{pdf_files[0][:-4]}-merged.pdf'

    return output


def merge_pdf(files: Optional[List[str]] = None,
              output: Optional[str] = None) -> bool:
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
