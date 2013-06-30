# coding=utf-8
import os
from smallinvoice import Smallinvoice

TEST_API_TOKEN = os.environ['TEST_API_TOKEN']


def get_smallinvoice():
    return Smallinvoice(TEST_API_TOKEN)


def generate_address():
    from smallinvoice.clients import Address

    return Address(primary=1, street="Kernstrasse", streetno="60", city="Zurich",
                   code="8004", country="CH")


def generate_customer(name="Hanspeter Muster"):
    from smallinvoice.clients import Customer, CUSTOMER_TYPE, CUSTOMER_GENDER

    return Customer(address_type=CUSTOMER_TYPE.PRIVATE, gender=CUSTOMER_GENDER.MALE,
                    name=name, language="de")