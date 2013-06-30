# coding=utf-8
import json, collections


class PREVIEW_SIZE(object):
    SMALL = 240
    MEDIUM = 600
    BIG = 825
    HUGE = 1240


class REQUEST_METHOD(object):
    AUTO = 0
    POST = 1
    GET = 2


class SmallInvoiceException(Exception):
    """ Base class for all exceptions raised by smallinvoice """

    def __init__(self, message):
        final_message = "smallinvoice-client exception: %s" % message
        super(Exception, self).__init__(final_message)


class SmallInvoiceConfigurationException(SmallInvoiceException):
    """ Thrown when the client is not properl configurated"""

    def __init__(self, client):
        message = "Wrong configuration.: " \
                  "token: %s" % (client.api_token,)
        super(SmallInvoiceException, self).__init__(message)


class SmallInvoiceConnectionException(SmallInvoiceException):
    """ The client could not connect for any reason. """

    def __init__(self, status_code, remote_message):
        message = "Failed to Connect, Status %s; Message: %s" % (
            status_code, remote_message)
        super(SmallInvoiceException, self).__init__(message)


class Methods(object):
    LIST = "%s/list"
    GET = "%s/get/id/%s"
    ADD = "%s/add"
    DELETE = "%s/delete/id/%s"
    UPDATE = "%s/edit/id/%s"
    PDF = "%s/pdf/id/%s"
    PREVIEW = "%s/preview/id/%s/page/%s/size/%s"
    EMAIL = "%s/email/id/%s"
    STATUS = "%s/status/id/%s"


class BaseService(object):
    name = 'BASE_SERVICE'

    def __init__(self, client):
        self.client = client

    def all(self):
        return self.client.request_with_method(Methods.LIST % self.name)['items']

    def details(self, identifier):
        return self.client.request_with_method(Methods.GET % (self.name, identifier,))['item']

    def add(self, data):
        return self.client.request_with_method(Methods.ADD % self.name, data=data)["id"]

    def delete(self, identifier):
        return self.client.request_with_method(Methods.DELETE % (self.name, identifier,),
                                               request_method=REQUEST_METHOD.POST)

    def update(self, identifier, data):
        return self.client.request_with_method(Methods.UPDATE % (self.name, identifier,),
                                               data=data)

    def pdf(self, identifier):
        """ returns the pdf from the object as binary data """
        return self.client.request_with_method(Methods.PDF % (self.name, identifier,))

    def preview(self, identifier, page_number, size):
        """ returns a preview from the object and the page with the specified size as binary data """
        return self.client.request_with_method(
            Methods.PREVIEW % (self.name, identifier, page_number, size,))

    def email(self, identifier, data):
        return self.client.request_with_method(Methods.EMAIL % (self.name, identifier,),
                                               data=data)

    def status(self, identifier, data):
        return self.client.request_with_method(Methods.STATUS % (self.name, identifier,),
                                               data=data)


class BaseJsonEncodableObject(object):
    """ This class can be easily encoded into a json string by calling encode, because smallinvoice excepts the json
        attributes to be in a certain order, we have to work with a ordered set as data representation.
    """

    def encode(self):
        return json.dumps(self.get_data(), indent=4)

    def get_data(self):
        if not hasattr(self, 'json_data'):
            self.json_data = collections.OrderedDict()
        return self.json_data

    def append_to(self, key, value):
        self.get_data()[key].append(value.get_data())

    def __setattr__(self, key, value):
        if key != 'json_data':
            self.get_data()[key] = value
        else:
            super(BaseJsonEncodableObject, self).__setattr__(key, value)

    def __getattr__(self, item):

        if item == 'json_data':
            return super(BaseJsonEncodableObject, self).__getattribute__(item)
        else:
            return self.get_data()[item]


class ObjectWithPositions(BaseJsonEncodableObject):
    def add_position(self, position):
        self.append_to('positions', position)


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