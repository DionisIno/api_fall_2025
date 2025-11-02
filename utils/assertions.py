from utils.logger import log


class Assertions:

    @log
    def assert_status_code(self, response, status_code):
        assert response.status_code == status_code, \
            f"Неверный статус код. Ожидали {status_code} статус, получили {response.status_code} статус"