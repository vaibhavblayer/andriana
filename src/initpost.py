import click
import 


post_type = ['equation', 'problem', 'python', 'swift']

@click.command(help='Creates post for social media')
@click.option('--post_type',prompt='Post type', type=click.Choice(post_type))
@click.option('--chapter', prompt='Chapter', type=click.Choice(chapters))
@click.option('--post_size', prompt='Size', type=click.Choice([[5, 5], [4.5, 8]]))
@click.option('-a', '--append_to_database', prompt='Append to database', is_flag=True, default='Yes', show_default=True,type=click.Choice(['Yes', 'No']))
def initpost(post_type, chapter, post_size):
    
    path_dir = f'10xphysics/testing/{}'
    if append_to_database:
        try:
            post_number = getData(chapter, post_type)[0][0]
        except:
            post_number = 1

        insertData(chapter, post_type)
    else:
        post_number = post_number_without_database

    path_dir = os.path.join(
            path_chapter(chapter.lower(), post_type),
            f'{post_type}-{post_number:02}'
            )
    os.makedirs(path_dir, exist_ok=True)
    path_tex = os.path.join(path_dir, 'main.tex')

    with open(path_tex, 'w') as file:
        file.write(r'\documentclass{article}')
        file.write(r'\usepackage{v-social-media}')
        file.write(f'\\geometry{{paperheight={post_size[0]}in, paperwidth={post_size[1]}in}}')
        file.write(f'\\geometry{{top={post_size[0]}in, bottom={post_size[1]}in}}')
        file.write(r'\begin{document}')
        file.write(f'{post_type}')
        file.write(r'\end{document}')

    
