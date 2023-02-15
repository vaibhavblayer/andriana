import click
import os
import time

from .tex.path_tex import path_chapter
from .tex.path_tex import chapters
from .database.insert_data import insertData
from .database.get_data import getData
from .database.database_functions import db_file
from .database.database_functions import create_connection
from .database.database_functions import createDatabase
from .print_functions import print_equation
from .print_functions import print_problem
from .print_functions import print_notes
from .print_functions import print_ideas
from .print_functions import bat_file
from .tex.equation_tex import equation_preamble
from .tex.equation_tex import equation_head
from .tex.equation_tex import equation_title


eqn_number_without_database = int(time.strftime("%H%M%S%d%m%Y"))

@click.command(
        help="Creates equation format tex file"
        )
@click.option(
        '-c',
        '--chapter',
        help="Chapter name",
        type=click.Choice(
            chapters,
            case_sensitive=False),
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
def notes(chapter, title, equation_number, append_to_database):
    if append_to_database:
        try:
            equation_number = getData(chapter, 'notes')[0][0] + 1
            #print(equation_number)
        except:
            equation_number = 1
            #print(1)
        insertData(chapter, 'notes')
    else:
        equation_number = eqn_number_without_database

    path_equation = os.path.join(
            path_chapter(chapter.lower(), 'notes'),
            f'notes-{equation_number:02}'
            )
    os.makedirs(path_equation, exist_ok=True)
    main_tex = os.path.join(path_equation, 'main.tex')
    with open(main_tex, 'w') as file:
        file.write(equation_preamble)

    print_equation(equation_number, chapter, main_tex)
    bat_file(main_tex)


