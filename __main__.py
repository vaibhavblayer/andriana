import click


from .src.instagram import instagram
from .src.youtube import youtube
from .src.live_sidecard import sidecard
from .src.pdftopng import pdftopng
from .src.add_background import addbackground
from .src.tex.extract_tex_env import extracttexenv
from .src.equation import equation
from .src.problem import problem
from .src.database.fetch_data import fetchdata
from .src.notes import notes
from .src.ideas import ideas
from .src.chatgpt import chatgpt
from .src.database.update_data import updateequation
from .src.database.update_data import updateproblem
from .src.database.update_data import updatenotes
from .src.database.update_data import updateideas
from .src.initcode import initcode
from .src.compresspdf import compresspdf
from .src.overlaypdf import overlaypdf
#from .src.pdf import pdf
from .src.archive import archive




CONTEXT_SETTINGS = dict(
        help_option_names = [
            '-h',
            '--help'
        ]
)

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass




main.add_command(archive)
main.add_command(overlaypdf)
main.add_command(compresspdf)
main.add_command(initcode)
main.add_command(updateideas)
main.add_command(updatenotes)
main.add_command(updateproblem)
main.add_command(updateequation)
main.add_command(equation)
main.add_command(problem)
main.add_command(instagram)
main.add_command(youtube)
main.add_command(sidecard)
main.add_command(pdftopng)
main.add_command(addbackground)
main.add_command(extracttexenv)
main.add_command(fetchdata)
main.add_command(notes)
main.add_command(ideas)
main.add_command(chatgpt)


if __name__ == '__main__':
    main()




