# coding=utf-8
import os

TEST_API_TOKEN = os.environ['TEST_API_TOKEN']

def get_client():
    from smallinvoice.client import Client
    return Client(TEST_API_TOKEN)


def generate_address():
    from smallinvoice.customers import Address
    return Address(primary=1, street="Kernstrasse", streetno="60", city="Zurich",
                code="8004", country="CH")


def generate_customer(name="Hanspeter Muster"):
    from smallinvoice.customers import Customer, CUSTOMER_TYPE, CUSTOMER_GENDER
    return Customer(address_type=CUSTOMER_TYPE.PRIVATE, gender=CUSTOMER_GENDER.MALE,
                 name=name, language="de")