# coding=utf-8
from smallinvoice import BaseJsonEncodableObject, BaseService, SmallinvoiceService


class Catalog(BaseJsonEncodableObject):
    def __init__(self, catalog_type, unit, name, cost_per_unit, vat=0):
        self.type = catalog_type
        self.unit = unit
        self.name = name
        self.cost_per_unit = cost_per_unit
        self.vat = vat


class CatalogService(BaseService):
    name = 'catalog'

SmallinvoiceService.register(CatalogService)