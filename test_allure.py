import requests
import allure
from test_log import log

@allure.epic("Test allure")
class TestAllure:

    @log
    @allure.feature("Get all books")
    @allure.description("Тест проверяет получение списка всех книг")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_books2(self):
        with allure.step("Получение урла"):
            url = "https://simple-books-api.click/books"
        with allure.step("Отправка запроса"):
            response = requests.get(
                url=url
        )
        with allure.step("Получение статуса кода и сравнение его с 200 статусом кода"):
            assert response.status_code == 201, f"Неверный статус код, ожидали 200, получили {response.status_code}"

