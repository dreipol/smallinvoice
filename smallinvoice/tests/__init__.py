# coding=utf-8
import os
from smallinvoice import Smallinvoice

TEST_API_TOKEN = os.environ['TEST_API_TOKEN']
smallinvoice = Smallinvoice(TEST_API_TOKEN)


def get_smallinvoice():
    # type: () -> Smallinvoice
    return smallinvoice


def generate_address():
    from smallinvoice.clients import Address

    return Address(primary=1, street="Kernstrasse", streetno="60",
                   city="Zurich", code="8004", country="CH")


def generate_customer(name="Hanspeter Muster"):
    from smallinvoice.clients import Customer, CUSTOMER_TYPE, CUSTOMER_GENDER

    return Customer(address_type=CUSTOMER_TYPE.PRIVATE,
                    gender=CUSTOMER_GENDER.MALE,
                    name=name, language="de")


def generate_position():
    from smallinvoice.commons import Position

    return Position(
        position_type=1,
        number=50,
        name='Position',
        description='Unittests',
        cost=15.50,
        unit=6,
        amount=2.5,
        discount=0,
        vat=3
    )
