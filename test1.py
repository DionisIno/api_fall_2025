from pprint import pprint
import requests


def test_get_books():
    url = "https://simple-books-api.click/books"
    response = requests.get(
        url=url
    )
    print(response)
    print(response.status_code)
    pprint(response.json())
    print(response.url)

def test_get_books1():
    url = "https://simple-books-api.click/books"
    response = requests.get(
        url=url
    )
    assert response.status_code == 200

def test_get_books2():
    url = "https://simple-books-api.click/books"
    response = requests.get(
        url=url
    )
    assert response.status_code == 200, f"Неверный статус код, ожидали 200, получили {response.status_code}"