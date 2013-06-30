# coding=utf-8
from smallinvoice.commons import BaseJsonEncodableObject, BaseService


class Letter(BaseJsonEncodableObject):
    def __init__(self, client_id, client_address_id, date, title):
        self.client_id = client_id
        self.client_address_id = client_address_id
        self.date = date
        self.title = title


class LetterState(BaseJsonEncodableObject):
    DRAFT = 7
    SENT = 1

    def __init__(self, status):
        self.status = status


class LetterService(BaseService):
    name = 'letter'

