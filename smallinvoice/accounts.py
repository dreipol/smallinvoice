# coding=utf-8
from smallinvoice.commons import BaseJsonEncodableObject, BaseService, Methods


class Account(BaseJsonEncodableObject):
    def __init__(self, title, institute, number, iban, swiftbic, clearing, postaccount, lsv, dd, esr):
        self.title = title
        self.institute = institute
        self.number = number
        self.iban = iban
        self.swiftbic = swiftbic
        self.clearing = clearing
        self.postaccount = postaccount
        self.lsv = lsv
        self.dd = dd
        self.esr = esr


class AccountService(BaseService):
    name = 'account'

    def details(self, identifier):
        """
        this webserice does not return the default dictionary containing the data in the item key, instead it
        returns the data directly.
        """
        return self.client.request_with_method(Methods.GET % (self.name, identifier,))