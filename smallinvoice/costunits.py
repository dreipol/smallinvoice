# coding=utf-8
from smallinvoice import BaseJsonEncodableObject, BaseService, SmallinvoiceService


class Costunit(BaseJsonEncodableObject):
    def __init__(self, name, status):
        self.name = name
        self.status = status


class CostUnitService(BaseService):
    name = 'costunit'

SmallinvoiceService.register(CostUnitService)