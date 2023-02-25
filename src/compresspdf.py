import click
import os
import time
from PyPDF2 import PdfReader, PdfWriter

@click.command(
        help="Comresses the pdf files"
        )
@click.option(
        '-i',
        '--inputfile',
        type=click.Path(),
        default="./main.pdf",
        help="Input file name"
        )
@click.option(
        '-o',
        '--outputfile',
        type=click.Path(),
        default="./main_compressed.pdf",
        help="Output file name"
        )
def compresspdf(inputfile, outputfile):
    time_init = int(time.strftime('%s'))
    n_pages = 0

    reader = PdfReader(inputfile)
    writer = PdfWriter()

    for page in reader.pages:
        page.compress_content_streams()  # This is CPU intensive!
        writer.add_page(page)

    with open(outputfile, "wb") as f:
        writer.write(f)


