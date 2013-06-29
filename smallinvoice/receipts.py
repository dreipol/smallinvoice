# coding=utf-8
from smallinvoice import BaseJsonEncodableObject, ObjectWithPositions, BaseService, SmallinvoiceService


class Receipt(ObjectWithPositions):
    def __init__(self, client_id, client_address_id, currency, date, language):
        self.client_id = client_id
        self.client_address_id = client_address_id
        self.currency = currency
        self.date = date
        self.language = language
        self.positions = []


class ReceiptState(BaseJsonEncodableObject):
    DRAFT = 0
    SENT = 1
    PAID = 10

    def __init__(self, status):
        self.status = status


class ReceiptService(BaseService):
    name = 'receipt'

SmallinvoiceService.register(ReceiptService)