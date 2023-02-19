import click
import os


r_jee_test_paper = r"""\documentclass{article}
\usepackage{v-test-paper}
%\renewcommand{\ans}{\quad}
%\def\ansint#1{\quad}
\title{Module-Test-11\\(Physics-JEE)}

\begin{document}
\maketitle

\jeeSectionA
\begin{enumerate}
\item This is an objective type problem.
    \begin{tasks}(1)
        \task always\ans
        \task only 
        \task only 
        \task only 
    \end{tasks}
\end{enumerate}

\jeeSectionB
\begin{enumerate}\addtocounter{enumi}{20}
\item This is an integer type problem. \ansint{0}
\end{enumerate}
\end{document}"""


r_neet_test_paper = r"""\documentclass{article}
\usepackage{v-test-paper}
%\renewcommand{\ans}{\quad}
\title{Module-Test-11\\(Physics-NEET)}

\begin{document}
\maketitle

\neetSectionA
\begin{enumerate}
\item This is an objective type problem.
    \begin{tasks}(2)
        \task always\ans
        \task only 
        \task only 
        \task only 
    \end{tasks}
\end{enumerate}

\neetSectionB
\begin{enumerate}\addtocounter{enumi}{35}
\item This is section-B.
    \begin{tasks}{2}
        \task \ans
        \task   
        \task
        \task
    \end{tasks}
\end{enumerate}
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
    os.makedirs(f'{directory}/{pattern.lower()}', exist_ok = True)
    x = os.path.join(f'{directory}/{pattern.lower()}', "main.tex")
    with open(x, 'w') as fp:
        if pattern == 'JEE':
            fp.write(r_jee_test_paper)
        else:
            fp.write(r_neet_test_paper)

    click.echo(
            f'Initiated in the directory {directory}.'
    )






