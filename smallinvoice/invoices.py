# coding=utf-8
from smallinvoice.commons import ObjectWithPositions, BaseJsonEncodableObject, BaseService


class Invoice(ObjectWithPositions):
    def __init__(self, client_id, client_address_id, currency, date, due,
                 language):
        self.client_id = client_id
        self.client_address_id = client_address_id
        self.currency = currency
        self.date = date
        self.due = due
        self.language = language


class Payment(BaseJsonEncodableObject):
    def __init__(self, amount, date, payment_type):
        self.amount = amount
        self.date = date
        self.type = payment_type


class InvoiceState(BaseJsonEncodableObject):
    DRAFT = 0
    SENT = 1
    PAID = 2
    REMINDER = 3

    def __init__(self, status):
        self.status = status


class InvoiceService(BaseService):
    name = 'invoice'

    def payment(self, invoice_id, payment):
        return self.client.request_with_method('invoice/payment/id/%s' % (invoice_id,),
                                               data=payment)
