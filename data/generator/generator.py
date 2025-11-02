from faker import Faker
from data.dataclasses.registered_data import RegisteredDataClass

class Generator:
    fake = Faker()

    def registered_data(self):
        yield RegisteredDataClass(
            clientName=self.fake.name(),
            clientEmail=self.fake.email()
        )
