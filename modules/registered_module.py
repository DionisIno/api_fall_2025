from modules.base_module import BaseModule
from utils.logger import log


class RegisteredModule(BaseModule):

    @log
    def prepare_data(self, schema, data):
        """
        Подготавляваем данные для запроса на основе схемы
        """
        prepare_data = schema(
            clientName=data.clientName,
            clientEmail=data.clientEmail
        ).model_dump_json()
        return prepare_data