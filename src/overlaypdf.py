import click

from PIL import Image, ImageFont, ImageDraw
import math

@click.command(
        help="Overlays text and any pdf file"
        )
@click.option(
        '-i',
        '--inputfile',
        show_default=True,
        type=click.Path(),
        help="Inputfile path"
        )
@click.option(
        '-o',
        '--outputfile',
        show_default=True,
        type=click.Path(),
        help="Outputfile path"
        )
@click.option(
        '-p',
        '--position',
        default=[50, 50, 50, 50],
        type=click.Tuple([int, int, int, int]),
        show_default=True,
        help="Position of corners of background rectangle"
        )
@click.option(
        '-t',
        '--text',
        help="Text to be overlayed"
        )
def overlaypdf(inputfile, outputfile):
    image = Image.open("main-5.png")
    draw = ImageDraw.Draw(image)
    text = 'LAUGHING IS THE \n BEST MEDICINE'
    size = image.size
    font = ImageFont.truetype('Courier', 50)

    draw.rectangle([(50, size[1]-50), (size[0]-50, size[1]-200)], fill ="red")
    draw.text((size[0]*0.5, size[1]-125), text, fill ="black", font=font, align ="center", anchor="ms")
    #draw.multiline_text((size[0]*0.5, size[1]-125), text, fill ="black",direction="ttb", font=font, align ="center", anchor="ms")
    image.show()

