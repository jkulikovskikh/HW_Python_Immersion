'''
Hапишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
* имя файла без расширения или название каталога,
* расширение, если это файл,
* флаг каталога,
* название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
'''

import logging
import os
from collections import namedtuple
import argparse

parser = argparse.ArgumentParser(description='Get folder contents') 
parser.add_argument('path', metavar='path', type=str, nargs=1, help='') 
args = parser.parse_args() 

logging.basicConfig(filename='task_2.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger('task_2.log')

FOLDER = namedtuple('FOLDER', 'name_folder extension flag_folder name_parent_folder')


def get_folder_contents(folder):
    for root, dirs, files in os.walk(folder):
        for dir in dirs:
            name_dir, _ = os.path.splitext(os.path.basename(dir))
            logger.info(f'{FOLDER(name_dir, _, True, root)}')
        for file in files:
            name_file, ext_file = os.path.splitext(os.path.basename(file))
            logger.info(f'{FOLDER(name_file, ext_file, False, root)}')
    return 
    

print(get_folder_contents(*args.path))