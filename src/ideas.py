import click
import os
import time

from .tex.path_tex import path_chapter
from .tex.path_tex import chapters
from .database.insert_data import insertData
from .database.get_data import getData
from .print_functions import print_ideas
from .print_functions import bat_file


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
        '-i',
        '--idea',
        type=click.STRING,
        default="Andriana"
        )
@click.option(
        '-n',
        '--ideas_number',
        type=click.INT
        )
@click.option(
        '-a',
        '--append_to_database',
        is_flag=True,
        help="flag (-a turns-on) appends the equation to database"
        )
def ideas(chapter, idea, ideas_number, append_to_database):
    if append_to_database:
        try:
            ideas_number = getData(chapter, 'ideas')[0][0] + 1
        except:
            ideas_number = 1
        insertData(chapter, 'ideas')
    else:
        ideas_number = eqn_number_without_database

    path_equation = os.path.join(
            path_chapter(chapter.lower(), 'ideas'),
            f'ideas-{ideas_number:02}'
            )
    os.makedirs(path_equation, exist_ok=True)
    main_txt = os.path.join(path_equation, 'main.txt')
    with open(main_txt, 'w') as file:
        file.write(idea)

    print_ideas(ideas_number, chapter, main_txt)
    bat_file(main_txt)


