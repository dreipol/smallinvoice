# coding=utf-8
from smallinvoice.commons import BaseJsonEncodableObject, BaseService


class ACCOUNT_TYPE(object):
    IBAN = 'IBAN'


class ACCOUNT_DEFAULT(object):
    YES = 1
    NO = 0


class ClientAccount(BaseJsonEncodableObject):
    def __init__(self, number, swift, clearing, type=ACCOUNT_TYPE.IBAN, default=ACCOUNT_DEFAULT.YES, name=None):
        self.type = type
        self.number = number
        self.clearing = clearing
        self.swift = swift
        self.name = name
        self.default = default


class ClientAccountService(BaseService):
    name = 'clientaccount'
    
    def all(self, client_identifier):
        return self.client.request_with_method('{0}/list/client_id/{1}'.format(self.name, client_identifier))['items']
    
    def add(self, client_identifier, client_account):
        return self.client.request_with_method(
            '{0}/add/client_id/{1}'.format(self.name, client_identifier), data=client_account)['id']
    
    def update(self, client_identifier, client_account, client_account_id):
        client_account.id = client_account_id
        return self.client.request_with_method(
            '{0}/edit/id/{1}/client_id/{2}'.format(self.name, client_account_id, client_identifier, ),
            data=client_account)
    
    def delete(self, client_identifier, client_account_identifier):
        return self.client.request_with_method(
            '{0}/delete/id/{1}/client_id/{2}'.format(self.name, client_account_identifier, client_identifier))
    
    def get(self, client_identifier, client_account_identifier):
        return self.client.request_with_method(
            '{0}/get/id/{1}/client_id/{2}'.format(self.name, client_account_identifier, client_identifier))['item']
