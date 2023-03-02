import sys
import openai
import click
import os
import time
from rich.console import Console

# Set the API key
openai.api_key = os.environ["OPENAI_API_KEY"]

from typing import List
from rich.console import Console, OverflowMethod


path_gpt_temp = '/Users/vaibhavblayer/10xphysics/chatgpt_posts/temp'

def create_post(question, answer, Q, A, q_color, a_color, b_color, minted_code, language, minted_style):
    path_gpt = '/Users/vaibhavblayer/10xphysics/chatgpt_posts/temp'
    os.makedirs(path_gpt)
    main_tex = os.path.join(path_gpt, 'main.tex')
    with open(main_tex, 'w') as file:
        file.write(f'\\documentclass{{article}}\n')
        file.write(f'\\usepackage{{v-square-equation}}\n')
        if minted_code == True:
            file.write(f'\\usemintedstyle{{{minted_style}}}\n')
            main_py = os.path.join(path_gpt, 'main.py')
            with open(main_py, 'w') as pyfile:
                pyfile.write(answer)
        file.write(f'\\begin{{document}}\n')
        if b_color != 'paper':
            file.write(f'\\pagecolor{{{b_color}}}\n')
        #file.write(f'\\boldmath\n')
        file.write(f'\\ttfamily\n')
        file.write(f'\\sloppy\n')
        file.write(f'\\vspace*{{\\fill}}\n')
        file.write(f'\\begin{{itemize}}\n')
        file.write(f'\t\\item[\\textcolor{{{q_color}}}{{{Q}}}]\\textcolor{{{q_color}}}{{{question}}}\n\n')
        if minted_code == False:
            file.write(f'\t\\item[\\textcolor{{{a_color}}}{{{A}}}]\\textcolor{{{a_color}}}{{{answer.strip()}}}\n')
        else:
            file.write(f'\t\\item[\\textcolor{{{a_color}}}{{{A}}}]\n')
            file.write(f'\\begin{{minted}}[tabsize=4, breaklines, mathescape]{{{language}}}\n')
            file.write(f'{answer}\n')
            file.write(f'\\end{{minted}}\n')

        file.write(f'\\end{{itemize}}\n')
        file.write(f'\\vspace*{{\\fill}}\n')
        file.write(r"\end{document}")
    os.system(f'bat {main_tex}')
    #click.pause()

def render(path_gpt_temp, question, b_color):
    os.chdir(path_gpt_temp)
    try:
        os.system(f'pdflatex -shell-escape main.tex')
        click.pause()
        try:
            os.system(f'andriana pdftopng -t -d 320')
            if b_color == 'paper':
                try:
                    os.system(f'andriana addbackground')
                    try:
                        output_file_name  = create_file_using_string(question, "png")
                        os.system(f'cp new.png ../{output_file_name}')
                    except:
                        print('Error')
                except:
                    print('Error')
            else:
                try:
                    output_file_name  = create_file_using_string(question, "png")
                    os.system(f'cp main.png ../{output_file_name}')
                    print(f'\n\tOutput is rendered as {output_file_name}\n')
                except:
                    print('Error')

            try:
                os.system(f'rm -r {path_gpt_temp}')
            except:
                print('Error')
        except:
            print('Error')
    except:
        print('Error')


def create_file_using_string(string: str, ext: str) -> str:
    list_string = string.strip().lower().rstrip('.?!').split()
    connector = '_'
    time_date = f'{time.strftime("%H%M%S"):06}_{time.strftime("%d%m%Y"):08}'
    output_file = f'{connector.join(list_string[:])}_{time_date}.{ext}'
    return output_file

def create_output_file(ext: str)->str:
    output_file = f'{time.strftime("%H%M%S"):06}_{time.strftime("%d%m%Y"):08}.{ext}'
    return output_file

@click.command(
        help='Ask anything and export the result as png or any other file format'
        )
@click.option(
        '-q',
        '--question',
        default='What is chatGPT ?',
        show_default=True,
        help="Ask anything"
        )
@click.option(
        '-r',
        '--read',
        is_flag = True,
        default=False,
        show_default=True,
        help="If on! Siri reads the result"
        )
@click.option(
        '-e',
        '--extension',
        default="txt",
        show_default=True,
        help="File extension for saving output"
        )
@click.option(
        '-p',
        '--post',
        is_flag=True,
        default=False,
        show_default=True,
        help="If given [-p] then result will be rendered as png"
        )
@click.option(
        '-Q',
        '--q_symbol',
        default="$\\Omega ~.$",
        show_default=True,
        help='Question symbol'
        )
@click.option(
        '--q_color',
        default='GREEN10',
        show_default=True,
        help='Question color'
        )
@click.option(
        '-A',
        '--a_symbol',
        default="$\\lambda ~.$",
        show_default=True,
        help='Answer symbol'
        )
@click.option(
        '--a_color',
        default='WHITE01',
        show_default=True,
        help='Answer color'
        )
@click.option(
        '-b',
        '--bgcolor',
        default='BLUE20',
        show_default=True,
        help="Background color"
        )
@click.option(
        '-R',
        '--rendering',
        is_flag=True,
        help="Flag for rendering"
        )
@click.option(
        '-m',
        '--minted_code',
        is_flag=True,
        help="Turn on this flag for minted_code"
        )
@click.option(
        '-l',
        '--language',
        default='python',
        help='Language for minted_code'
        )
@click.option(
        '-M',
        '--minted_style',
        type=click.Choice(['algol', 'fruity', 'monokai', 'xcode']),
        default='fruity',
        show_default=True,
        help='Minted style'
        )
def chatgpt(question, read, extension, post, q_symbol, q_color, a_symbol, a_color, bgcolor, rendering, minted_code, language, minted_style):
    question = question
    answer = get_ans_gpt(question)
    path_gpt = '/Users/vaibhavblayer/10xphysics/chatgpt'
    main_txt = os.path.join(path_gpt, create_file_using_string(question, extension))
    with open(main_txt, 'w') as file:
        if extension == 'py':
            file.write(f'"""\n\nQ. {question}\n\n"""')
        elif extension == 'swift':
            file.write(f'/*\n\nQ. {question}\n\n*/')
        elif extension == 'tex':
            file.write(f'\iffalse\n\nQ. {question}\n\n\\fi')
        else:
            file.write(f'Q. {question}')
        file.write(answer)


    overflow_methods: List[OverflowMethod] = [question]
    console = Console(width=max_len(main_txt))
    print('\n')
    for overflow in overflow_methods:
        console.rule(overflow)
        console.print(answer.strip(), overflow=overflow, style="deep_pink2")
        console.print()

    if read:
        os.system(f'say -f {main_txt}')
    
    click.pause()
    if post == True:
        if bgcolor == 'paper':
	        post_args = {
	                'question': question,
	                'answer': answer,
	                'Q': q_symbol,
	                'A': a_symbol,
	                'q_color': 'REDD',
	                'a_color': 'black',
	                'b_color': bgcolor,
	                'minted_code': minted_code,
	                'language': language,
	                'minted_style': 'xcode'
	                }
        else:
            post_args = {
	                'question': question,
	                'answer': answer,
	                'Q': q_symbol,
	                'A': a_symbol,
	                'q_color': q_color,
	                'a_color': a_color,
	                'b_color': bgcolor,
	                'minted_code': minted_code,
	                'language': language,
	                'minted_style': minted_style
	                }



        create_post(**post_args)
        if rendering == True:
            render(path_gpt_temp, question, bgcolor)


def get_ans_gpt(prompt):
    model_engine = ["code-davinci-002", "text-davinci-003", "code-cushman-001", "text-curie-001"]
    #model_engine = 'text-{}-003'.format("davinci")
    completion = openai.Completion.create(
            engine=model_engine[1],
            prompt=prompt,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.2
            )
    message = completion.choices[0].text
    return message


def max_len(file):
    file = open(file, 'r')
    max_len = 0
    longest_line = ""

    for line in file:
        line_len = len(line)
        if line_len > max_len:
            max_len = line_len
            longest_line = line
    file.close()
    cols = os.get_terminal_size()[0]
    if max_len > cols:
        return cols
    else:
        return max_len



