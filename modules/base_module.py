from utils.logger import log

class BaseModule:

    @log
    def create_request_body(self, schema, data_class_instance):
        data_dict = {
            key: value for key, value in data_class_instance.__dict__.items()
        }
        return schema(**data_dict).model_dump_json()


    @log
    def create_url(self, func, endpoint: str, **kwargs) -> str:
        return func(endpoint, **kwargs)