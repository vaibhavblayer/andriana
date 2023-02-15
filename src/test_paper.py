import click
import os
import time



r_test_paper = r"""\documentclass{article}
\usepackage{v-test-paper}
\begin{document}
\end{document}"""


@click.command(
        help="Creates templates for JEE/NEET test paper"
        )
@click.option(
        '-d',
        '--directory', 
        help="directory"
)
@click.option(
        '-p', 
        '--pattern',
        type=click.Choice(
            ['JEE', 'NEET'],
            case_sensitive=False
        ),
        default="JEE",
        help="JEE or NEET"
)
def testpaper(directory, pattern):
    os.makedirs(f'{directory}', exist_ok = True)
    x = os.path.join(f'{directory}', "main.tex")
    with open(x, 'w') as fp:
        fp.write(r_test_paper)

    click.echo(
            f'Initiated in the directory {directory}.'
    )



















#    with click.progressbar([1, 2, 3]) as bar:
#        for x in bar:
#            print(f"sleep({x})...")
#            time.sleep(x)





