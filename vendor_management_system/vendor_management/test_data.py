# from vendor_management.test_data import *
from faker import Faker
from .models import Vendor


def create_dummy_vendors(n=20):
    fake = Faker('en_IN')

    for _ in range(n):
        name = fake.unique.first_name().strip()
        contact_details = fake.unique.phone_number()

        Vendor.objects.create(
            name=name,
            contact_details=contact_details,
            address=fake.address(),
        )
