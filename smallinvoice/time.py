# coding=utf-8
from smallinvoice.commons import BaseJsonEncodableObject, BaseService


class Time(BaseJsonEncodableObject):
    def __init__(self, start, end, date):
        self.start = start
        self.end = end
        self.date = date


class TimeService(BaseService):
    name = 'time'