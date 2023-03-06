import click
import os

@click.command(help='archives the path directory to the destination and delete recursively')
@click.option('-d', '--directory', type=click.Path(), default="./temp")
@click.option('-D', '--destination', type=click.Path())
def archive(directory, destination):
    try:
        os.system(f'cp -r {directory} {destination}')
        print(f'\tSuccessfully {directory} copied recursively into {destination}')
        try:
            os.system(f'rm -r {directory}')
            print(f'\tSuccessfully {directory} deleted recursively.')
        except:
            print(f'Failed deletion of {directory}')
    except:
        print(f'Failed archiving of {directory} into {desination}')



