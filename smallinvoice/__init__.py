# coding=utf-8
import json, collections
__author__ = 'phil'


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



