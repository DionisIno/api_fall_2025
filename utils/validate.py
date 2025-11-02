from utils.logger import log


class Validate:

    @log
    def validate(self, response, schema):
        """
        Валидирует тело ответа на остновании переданной схемы
        :param response: тело ответа
        :param schema: схема для валидации
        :return: bool
        """
        try:
            schema.model_validate(response.json())
        except ValueError as e:
            raise ValueError(f"Invalid response format in {e}")