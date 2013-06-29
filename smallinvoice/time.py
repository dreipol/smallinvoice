# coding=utf-8
from smallinvoice import BaseJsonEncodableObject, BaseService, SmallinvoiceService


class Time(BaseJsonEncodableObject):

    def __init__(self, start, end, date):
        self.start = start
        self.end = end
        self.date = date


class TimeService(BaseService):
    name = 'time'


SmallinvoiceService.register(TimeService)