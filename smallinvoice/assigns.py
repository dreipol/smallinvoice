# coding=utf-8
from smallinvoice.commons import BaseJsonEncodableObject, BaseService


class Assign(BaseJsonEncodableObject):
    def __init__(self, assign_type, type_id, hours, date):
        self.type = assign_type
        self.type_id = type_id
        self.hours = hours
        self.date = date


class AssignService(BaseService):
    name = 'assign'