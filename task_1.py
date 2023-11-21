'''
Дорабатываем задачу 4. Добавьте регистрацию возможных ошибок. 
Добавьте возможность запуска из командной строки с использованием библиотеки argparse
'''

import logging
from datetime import datetime, date
from collections import namedtuple
import argparse

parser = argparse.ArgumentParser(description='Get date') 
parser.add_argument('text', metavar='text', type=str, nargs=1, help='') 
args = parser.parse_args() 

logging.basicConfig(filename='task_1.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger('task_1.log')

MONTHS = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12
}
WEEKDAYS = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6
}

DATE = namedtuple('DATE', 'day month year')

def get_date(text):
    try:
        num_week, week_day, months = text.split()
        num_week = int(num_week.split('-')[0])
        week_day = WEEKDAYS[week_day]
        months = MONTHS[months]
    except ValueError as e:
        logger.error(f'Вызывается ошибка ValueError: {e}')
    except KeyError as e:
        logger.error(f'Вызывается ошибка KeyError: {e}')
    else:
        count_week = 0
        for i_day in range(1, 31 + 1):
            try:
                d = date(year=datetime.now().year, month=months, day=i_day)
            except ValueError as e:
                logger.error(f'Вызывается ошибка ValueError: {e}')
            else:   
                if d.weekday() == week_day:
                    count_week += 1
                    if count_week == num_week:
                        logger.info(f'{DATE(d.day, d.month, d.year)}')
                        return d

print(get_date(*args.text))