import csv

import loguru

from .models import (
    Author,
    Publisher,
    Genre,
    Language,
    Format,
    Condition,
    Book,
    BookInstance,
)


START_FILES = {
    'book_titles': 'bookworm/start_here/title.csv',
    'isbn': 'bookworm/start_here/isbn.csv',
}


def compile_start_books():
    with open('restaurant/start_here/start_inventory.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            try:
                if '#' in row[0]:
                    continue
                elif len(row) != 4:
                    loguru.logger.error(f'check ingredient on line {reader.line_num}, {row}')
                else:
                    Ingredient.objects.get_or_create(
                        item_name=row[0],
                        on_hand=row[1],
                        unit_type=row[2],
                        unit_cost=row[3],
                    )
            except Exception as err:
                loguru.logger.error(f"{err}, line {reader.line_num}")