import click
import os
import sys
import itertools
import pdf2image
from .tex.functions_tex import create_files

@click.command(
        help="Converts pdf pages into pngs"
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
        default="./main.png",
        help="Output file name"
        )
@click.option(
        '-d',
        '--dpi',
        default=320,
        type=click.INT,
        help="DPI -> density per inch for png"
        )
@click.option(
        '-t',
        '--transparent',
        is_flag=True,
        default=False,
        help="Use this flag for transparent png"
        )
def pdftopng(inputfile, outputfile, dpi, transparent):
    #os.makedirs(f'{directory}', exist_ok = True)

    pages = pdf2image.convert_from_path(
        "./{}".format(inputfile), 
        dpi=dpi,
        transparent = transparent,
        use_pdftocairo = True
        )

    for page in pages:
        file_name = create_files(
                outputfile, 
                pages.index(page), 
                len(pages), 
                'png'
                )

        page.save('{0}'.format(file_name), 'PNG')
        print(f'{inputfile} page {pages.index(page)+1} -> {file_name}')



