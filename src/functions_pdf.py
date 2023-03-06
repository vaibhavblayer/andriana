from .tex.functions_tex import create_files

def pages_pdf(inputfile):

    from PyPDF2 import PdfReader

    file = open(inputfile, 'rb')
    pdfReader = PdfReader(file)
    return len(pdfReader.pages)



def extract_png_pdf(inputfile, first_page, last_page, outputfile, dpi, transparent):
    """
    keyword args:
        inputfile <- Path
        first_page <- Int
        last_page <- Int
        outputfile <- Path
        dpi <- Int
        transparent <- Bool
    """

    from PyPDF2 import PdfReader
    from pdf2image import convert_from_path

    pages = convert_from_path(
            "./{}".format(inputfile), 
            first_page=first_page,
            last_page=last_page,
            dpi=dpi,
            transparent = transparent,
            use_pdftocairo = True,
            thread_count=8
            )
    file = open(inputfile, 'rb')
    pdfReader = PdfReader(file)
    n_pages = len(pdfReader.pages)

    for i in range(first_page, last_page+1):
        file_name = create_files(
                outputfile,
                i-1,
                n_pages,
                'png'
                )
        pages[i-first_page].save(f'{file_name}', 'PNG')
        print(f'{inputfile} page {i} -> {file_name}')

