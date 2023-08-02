import csv
import json

import loguru

# from .models import Author, Publisher, Genre, Language, Format, Condition, Book, BookInstance
from backend.APIGoogleBooks import GoogleBooksAPI


START_FILES = {
    'title': '../start_here/title.csv',
    'isbn': '../start_here/isbn.csv',
}


def add_isbn_prefix(isbn: str) -> str:
    """ Add 978 prefix to 10 digit ISBNs """

    isbn = isbn.replace('-', '')
    if len(isbn) == 10:
        return '978' + isbn
    return isbn


# def compile_start_books():
#     with open(START_FILES['title']) as csvfile:
#         reader = csv.reader(csvfile)
#         next(reader, None)
#         for row in reader:
#             try:
#                 if '#' in row[0]:
#                     continue
#                 elif len(row) != 4:
#                     loguru.logger.error(f'check ingredient on line {reader.line_num}, {row}')
#                 else:
#                     Ingredient.objects.get_or_create(
#                         item_name=row[0],
#                         on_hand=row[1],
#                         unit_type=row[2],
#                         unit_cost=row[3],
#                     )
#             except Exception as err:
#                 loguru.logger.error(f"{err}, line {reader.line_num}")


def get_isbns() -> list:
    with open(START_FILES['isbn']) as csvfile:
        reader = csv.reader(csvfile)
        isbns = [row[0] for row in reader]

    return isbns


def compile_start_data():
    isbns = get_isbns()
    books_api = GoogleBooksAPI()
    for isbn in isbns:
        # isbn = add_isbn_prefix(isbn)
        response = books_api.get_from_isbn(isbn)
        # print(json.dumps(response, indent=4))
        if response:
            book_data = {key: val for key, val in response['items'][0]['volumeInfo'].items()}
            print(book_data)
            print(response['items'][0]['volumeInfo']['title'])
        else:
            loguru.logger.debug(f"no book for for isbn: {isbn}")


if __name__ == '__main__':
    print(compile_start_data())
