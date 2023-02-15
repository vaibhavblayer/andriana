import click
import os
import time
import sqlite3

from ..tex.path_tex import path_chapter
from ..tex.path_tex import path_mechanics
from ..tex.path_tex import path_electrodynamics


def updateData(chapter, post_type, title):
    path_database = os.path.join(
            path_chapter(
                chapter.lower(),
                post_type
                ),
            f'{post_type}.db'
            )
    database = sqlite3.connect(path_database)
    print(f'Databse {database} opened.\n')

    cursor = database.cursor()

    if post_type == 'equation':
        data_table= """ INSERT INTO equation(
            chapter,
            title
        )VALUES(?,?); """
        data=(chapter, title)
        cursor.execute(data_table, data)
        database.commit()

    elif post_type == 'problem':
        data_table= """ INSERT INTO problem(
            chapter
        )VALUES(?); """
        data=(chapter)
        cursor.execute(data_table, data)
        database.commit()

    elif post_type == 'notes':
        data_table= """ INSERT INTO notes(
            chapter
        )VALUES(?); """
        data=(chapter)
        cursor.execute(data_table, data)
        database.commit()

    elif post_type == 'ideas':
        data_table= """ INSERT INTO ideas(
            chapter
        )VALUES(?); """
        data=(chapter)
        cursor.execute(data_table, data)
        database.commit()

    database.close()





