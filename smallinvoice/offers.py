# coding=utf-8
from smallinvoice.commons import ObjectWithPositions, BaseJsonEncodableObject, BaseService


class Offer(ObjectWithPositions):
    def __init__(self, client_id, client_address_id, currency, date, due,
                 language):
        self.client_id = client_id
        self.client_address_id = client_address_id
        self.currency = currency
        self.date = date
        self.due = due
        self.language = language


class OfferState(BaseJsonEncodableObject):
    DRAFT = 0
    SENT = 1
    OK = 9
    REMINDER = 10

    def __init__(self, status):
        self.status = status


class OfferService(BaseService):
    name = 'offer'
