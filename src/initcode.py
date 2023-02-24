import click
import os
import time


def code_file(keyword, language):
    date = f'{time.strftime("%d%m%Y"):08}'
    path = f'/Users/vaibhavblayer/10xphysics/{language}/{date}_{keyword}'
    os.makedirs(path, exist_ok=True)
    lang_file =  'main.py'
    if language == 'python':
        lang_file = 'main.py'
    elif language == 'swift':
        lang_file = 'main.swift'
    elif language == 'c':
        lang_file = 'main.c'
    main_file = os.path.join(path, lang_file)

    return main_file


@click.command(
        help="Creates file with proper extension in proper directory."
        )
@click.option(
        '-t',
        '--title',
        type=click.STRING,
        help="title of the project or any relevent keyword"
        )
@click.option(
        '-l',
        '--language',
        default = 'python',
        help="Language for which project is being created."
        )
def initcode(title, language):
    main_file = code_file(title, language)
    if os.path.isfile(main_file) and os.path.getsize(main_file) > 0:
        os.system(f'vim {main_file}')
    else:
        with open(main_file, 'w') as file:
            file.write(f'"""\n\n{title}\n"""')
        os.system(f'vim {main_file}')



