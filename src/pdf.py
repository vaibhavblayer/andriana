import click

from .choice_option import ChoiceOption



@click.command()
@click.option(
        '--todo',
        prompt='What you wanna do:',
        type=click.Choice(['convert_to_png', 'annotate', 'compress']),
        cls=ChoiceOption
        )
def pdf(todo):

    if todo == 'convert_to_png':
        
        print("PDF")
