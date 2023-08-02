import json

import loguru
import requests

from config import settings


def parse_response(response: dict) -> list:
    """ removes unnecessary keys and convert to a list of dicts """
    result = []
    for book_info in response['items']:
        result.append({key: val for key, val in book_info['volumeInfo'].items()})

    return result


class GoogleBooksAPI:
    def __init__(self):
        self.BASE_API = settings.GOOGLE_BOOKS_BASE_API
        self.FIELDS_TO_GET = [
            'title',
            'authors',
            'publisher',
            'publishedDate',
            'description',
            'pageCount',
            'categories',
            'imageLinks',
        ]

    def __str__(self):
        return self.__class__.__name__

    def compile_url(self, query_type: str, user_input: str) -> str:
        url = ''.join([
            self.BASE_API,
            'volumes?q=',
            query_type,
            user_input,
            '&fields=items(volumeInfo(' + ','.join(self.FIELDS_TO_GET) + '))',
            '&orderBy=relevance',
            '&printType=BOOKS',
        ])

        return url

    def remove_spaces_from_title(self, title: str) -> str:
        return title.replace(' ', '%20')

    def get_from_isbn(self, isbn: str) -> list or None:
        url = self.compile_url('isbn:', isbn)
        response = requests.get(url)
        if response.status_code != 200:
            loguru.logger.debug(f"{self.__str__()}: {self.get_from_isbn.__name__}: "
                                f"response code: {response.status_code}")
            loguru.logger.debug(f"response: {response.content}")
        else:
            response = json.loads(response.content)  # convert to dict
            # return parse_response(response)
            return response
    def get_from_title(self, title: str) -> list or None:
        title = self.remove_spaces_from_title(title)
        url = self.compile_url('intitle:', title)
        print(url)

        response = requests.get(url)
        if response.status_code != 200:
            loguru.logger.debug(f"{self.__str__()}: {self.get_from_isbn.__name__}: "
                                f"response code: {response.status_code}")
            loguru.logger.debug(f"response: {response.content}")
        else:
            response = json.loads(response.content)  #convert to dict
            return parse_response(response)


if __name__ == '__main__':
    # isbn = '3-522-12800-1'
    isbn = '9780545069670'  # sorcerer's stone
    title = "Harry Potter and the Sorcerer"
    # result = GoogleBooksAPI().get_from_isbn(isbn)
    result = GoogleBooksAPI().get_from_title(title)
    print(len(result))
    print(json.dumps(result, indent=4))


