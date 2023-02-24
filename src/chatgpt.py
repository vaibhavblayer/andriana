import sys
import openai
import click
import os
import time
from rich.console import Console
console = Console(width=20)
# Set the API key
openai.api_key = os.environ["OPENAI_API_KEY"]
# Use the ChatGPT model to generate text

from typing import List
from rich.console import Console, OverflowMethod


def create_output_file(ext: str)->str:
    output_file = f'{time.strftime("%H%M%S"):06}_{time.strftime("%d%m%Y"):08}.{ext}'
    return output_file

@click.command()
@click.option(
        '-q',
        '--question',
        help="Defines any term"
        )
@click.option(
        '-r',
        '--read',
        is_flag = True,
        help="If on read the result"
        )
@click.option(
        '-e',
        '--extension',
        default="txt",
        help="File extension for saving output"
        )
def chatgpt(question, read, extension):
    question = question
    answer = get_ans_gpt(question)
    path_gpt = '/Users/vaibhavblayer/10xphysics/chatgpt'
    main_txt = os.path.join(path_gpt, create_output_file(extension))
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
