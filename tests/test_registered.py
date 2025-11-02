import requests
# from data.endpoints import Endpoints
# from data.generator.generator import Generator
# from modules.registered_module import RegisteredModule
# from utils.assertions import Assertions
from utils.schemas.registered_schema.request_schema import RegisteredRequestSchema
from utils.schemas.registered_schema.response_schema import TokenResponseSchema
# from utils.validate import Validate
from http import HTTPStatus as status
from tests import ctx


class TestRegistered:
    # generator = Generator()
    # module = RegisteredModule()
    # endpoint = Endpoints()
    # validate = Validate()
    # assertion = Assertions()

    # def test_registered_v1(self):
    #     user_info = next(self.generator.registered_data())
    #     request_body = self.module.prepare_data(
    #         schema=RegisteredRequestSchema,
    #         data=user_info
    #     )
    #     response = requests.post(
    #         url=f"{self.endpoint.base_url}{self.endpoint.api_client_url}",
    #         data=request_body
    #     )
    #     self.validate.validate(
    #         response=response,
    #         schema=TokenResponseSchema
    #     )
    #     self.assertion.assert_status_code(
    #         response=response,
    #         status_code=status.CREATED
    #     )
    #
    # def test_registered_v2(self):
    #     request_body = self.module.create_request_body(
    #         schema=RegisteredRequestSchema,
    #         data_class_instance=next(self.generator.registered_data())
    #     )
    #     response = requests.post(
    #         url=f"{self.endpoint.base_url}{self.endpoint.api_client_url}",
    #         data=request_body
    #     )
    #     self.validate.validate(
    #         response=response,
    #         schema=TokenResponseSchema
    #     )
    #     self.assertion.assert_status_code(
    #         response=response,
    #         status_code=status.CREATED
    #     )
    #
    #
    # def test_registered_v3(self, create_endpoint):
    #     request_body = self.module.create_request_body(
    #         schema=RegisteredRequestSchema,
    #         data_class_instance=next(self.generator.registered_data())
    #     )
    #     response = requests.post(
    #         url=f"{self.module.create_url(create_endpoint, self.endpoint.api_client_url)}",
    #         data=request_body
    #     )
    #     self.validate.validate(
    #         response=response,
    #         schema=TokenResponseSchema
    #     )
    #     self.assertion.assert_status_code(
    #         response=response,
    #         status_code=status.CREATED
    #     )

    def test_registered_v4(self, create_endpoint):
        request_body = ctx.module.create_request_body(
            schema=RegisteredRequestSchema,
            data_class_instance=next(ctx.generator.registered_data())
        )
        response = requests.post(
            url=f"{ctx.module.create_url(create_endpoint, ctx.endpoint.api_client_url)}",
            data=request_body
        )
        ctx.validate.validate(
            response=response,
            schema=TokenResponseSchema
        )
        ctx.assertion.assert_status_code(
            response=response,
            status_code=status.CREATED
        )