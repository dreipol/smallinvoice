# coding=utf-8
from smallinvoice.commons import BaseJsonEncodableObject, BaseService


class Address(BaseJsonEncodableObject):
    def __init__(self, primary, street, streetno, city, code, country,
                 street2=""):
        self.primary = primary
        self.street = street
        self.streetno = streetno
        self.street2 = street2
        self.city = city
        self.code = code
        self.country = country


class CUSTOMER_TYPE(object):
    COMPANY = 1
    PRIVATE = 2


class CUSTOMER_GENDER(object):
    MALE = 1
    FEMALE = 2


class Customer(BaseJsonEncodableObject):
    def __init__(self, address_type, gender, name, language):
        self.type = address_type
        self.gender = gender
        self.name = name
        self.language = language
        self.addresses = []

    def add_address(self, address):
        self.append_to('addresses', address)


class ClientService(BaseService):
    name = 'client'
