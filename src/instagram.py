import click
import os
import time
import sqlite3


r_insta_equation = r"""\documentclass{article}
\usepackage{v-instagram-equation}
\begin{document}
\end{document}"""

r_insta_problem = r"""\documentclass{article}
\usepackage{v-instagram-problem}
\begin{document}
\end{document}"""




@click.command(help="Creates Instagram Post")
@click.option('-c', '--chapter')
@click.option('-t', '--title')
@click.option('-r', '--record')
@click.option('-f', '--format', type=click.Choice(['EQUATION', 'PROBLEM'], case_sensitive=False))
def instagram(n, d):
    os.makedirs(f'{n}', exist_ok = True)
    x = os.path.join(f'{n}', "main.tex")
    with open(x, 'w') as fp:
        fp.write(r_insta)

    click.echo(f'Project is initiated in the directory {d}.')

#    with click.progressbar([1, 2, 3]) as bar:
#        for x in bar:
#            print(f"sleep({x})...")
#            time.sleep(x)







#database = sqlite3.connect("instantpost.db")
#print(f'Databse {database} opened.\n')
#
#
#def createTable():
#    database.execute(
#        """ CREATE TABLE equation(
#            id INT PRIMARY KEY NOT NULL,
#            topic TEXT NOT NULL,
#            title TEXT NOT NULL,
#        ); """
#        )
#
#
#print(f'Table is created in the database {database}\n')
#
#database.close()




