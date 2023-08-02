import csv
import json

import loguru

# from .models import (
#     Author,
#     Publisher,
#     Genre,
#     Language,
#     # Format,
#     Condition,
#     Book,
#     BookInstance,
# )
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


def get_isbns() -> list:
    with open(START_FILES['isbn']) as csvfile:
        reader = csv.reader(csvfile)
        isbns = [row[0] for row in reader]

    return isbns


# def insert_book_details(book_details: dict):
#     for author in book_details['authors']:
#         Author.objects.get_or_create(name=author.lower())
#     for cat in book_details['categories']:
#         Genre.objects.get_or_create(name=cat.lower())
#
#     Book.objects.get_or_create(
#         isbn=book_details['isbn'],
#         title=book_details['title'],
#         author='',  # TODO one to many
#         publisher=book_details['publisher'],
#         published_date=book_details['publishedDate'],
#         description=book_details['description'],
#         page_count=book_details['pageCount'],
#         genre='',  # TODO foreignkey
#         thumbnail=book_details['imageLinks']['smallThumbnail'],
#         language='',  # TODO
#         msrp=10,
#     )


def compile_start_data():
    isbns = get_isbns()
    books_api = GoogleBooksAPI()
    for isbn in isbns:
        response = books_api.get_from_isbn(isbn)
        if not response:
            loguru.logger.debug(f"no book data for isbn: {isbn}")
        elif not all (books_api.FIELDS_TO_GET) in response['items'][0]['volumeInfo']:
            loguru.logger.debug(f"fields missing for: {isbn}")
            loguru.logger.debug(response['items'][0]['volumeInfo'])
        else:
            print(json.dumps(response['items'][0]['volumeInfo'], indent=4))
            loguru.logger.info(f"adding {isbn} to db")
            book_details = {key: val for key, val in response['items'][0]['volumeInfo'].items()}
            book_details['isbn'] = isbn
            # insert_book_details(book_details)


if __name__ == '__main__':
    print(compile_start_data())
