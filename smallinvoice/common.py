# coding=utf-8
from smallinvoice import BaseJsonEncodableObject

class Recipient(BaseJsonEncodableObject):
    def __init__(self, cc, email, name):
        self.cc = cc
        self.email = email
        self.name = name

class Mail(BaseJsonEncodableObject):
    def __init__(self, subject, body, sendstatus, afterstatus):
        self.subject = subject
        self.body = body
        self.sendstatus = sendstatus
        self.afterstatus = afterstatus
        self.recipients = []

    def add_recipient(self, recipient):
        self.append_to('recipients', recipient)


class Position(BaseJsonEncodableObject):
    def __init__(self, position_type, number, description, cost, unit, amount, name="",
                 discount=None, vat=0):
        self.type = position_type
        self.number = number
        self.name = name
        self.description = description
        self.cost = cost
        self.unit = unit
        self.amount = amount
        self.discount = discount
        self.vat = vat