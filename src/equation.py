import click
import os
import time

from .tex.path_tex import path_chapter
from .tex.path_tex import chapters
from .database.insert_data import insertData
from .database.get_data import getData
from .print_functions import print_equation
from .print_functions import bat_file
from .tex.equation_tex import equation_vertical_preamble
from .tex.equation_tex import equation_square_preamble
from .tex.equation_tex import equation_head
from .tex.equation_tex import equation_title
from .choice_option import ChoiceOption

eqn_number_without_database = int(time.strftime("%H%M%S%d%m%Y"))

@click.command(
        help="Creates equation format tex file"
        )
@click.option(
        '-c',
        '--chapter',
        prompt="Chapters:",
        help="Chapter name",
        type=click.Choice(
            chapters,
            case_sensitive=False),
        cls=ChoiceOption
        )
@click.option(
        '-t',
        '--title',
        type=click.STRING,
        )
@click.option(
        '-n',
        '--equation_number',
        type=click.INT
        )
@click.option(
        '-a',
        '--append_to_database',
        is_flag=True,
        help="flag (-a turns-on) appends the equation to database"
        )
@click.option(
        '-f',
        '--equation_format',
        default='square',
        type=click.Choice(['square', 'vertical']),
        show_default=True,
        help="Format for equation rendering"
        )
def equation(chapter, title, equation_number, append_to_database, equation_format):
    if append_to_database:
        try:
            equation_number = getData(chapter, 'equation')[0][0] + 1
        except:
            equation_number = 1
        insertData(chapter, 'equation')
    else:
        equation_number = eqn_number_without_database

    path_equation = os.path.join(
            path_chapter(chapter.lower(), 'equation'),
            f'equation-{equation_number:02}'
            )
    os.makedirs(path_equation, exist_ok=True)
    main_tex = os.path.join(path_equation, 'main.tex')
    if equation_format == 'square':
        with open(main_tex, 'w') as file:
            file.write(equation_vertical_preamble)
    else:
        with open(main_tex, 'w') as file:
            file.write(equation_square_preamble)

    print_equation(equation_number, chapter, main_tex)
    bat_file(main_tex)
    print('opening texmaker ...')
    os.system(f'open -a texmaker {main_tex}')
    time.sleep(1)


