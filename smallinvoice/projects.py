# coding=utf-8
from smallinvoice import BaseJsonEncodableObject, BaseService, SmallinvoiceService


class Project(BaseJsonEncodableObject):
    def __init__(self, name, client_id):
        self.name = name
        self.client_id = client_id


class ProjectService(BaseService):
    name = 'project'


SmallinvoiceService.register(ProjectService)