"""
Этот модель содержит генераторы для создания тестовых данных
"""
from faker import Faker

from data.dataclasses.create_orders_data import CreateOrdesDataClass
from data.dataclasses.registered_data import RegisteredDataClass

class Generator:
    fake = Faker()

    def registered_data(self):
        yield RegisteredDataClass(
            clientName=self.fake.name(),
            clientEmail=self.fake.email()
        )

    def create_order_data(self):
        yield CreateOrdesDataClass(
            bookId=self.fake.random_int(min=3, max=5),
            customerName=self.fake.name()
        )