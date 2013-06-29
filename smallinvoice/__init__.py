# coding=utf-8
import json, collections, requests

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
            Methods.PREVIEW% (self.name, identifier, page_number, size,))

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


class SmallinvoiceService(object):
    """ A simple client wrapper for the smallinvoice.ch web service api"""
    country_code = None
    api_token = None

    def __init__(self, api_token):
        """initializes the object, requires the country code and a valid api_token"""

        # raises an exception if the parameters are not valid.
        if not api_token:
            raise SmallInvoiceConfigurationException(self)
        self.api_token = api_token

        from accounts import AccountService
        from assigns import AssignService
        from catalog import CatalogService
        from costunits import CostUnitService
        from clients import ClientService
        from letters import LetterService
        from offers import OfferService
        from projects import ProjectService
        from receipts import ReceiptService
        from time import TimeService
        from invoices import InvoiceService

        self.invoices = InvoiceService(self)
        self.clients = ClientService(self)
        self.offers = OfferService(self)
        self.receipts = ReceiptService(self)
        self.letters = LetterService(self)
        self.catalog = CatalogService(self)
        self.projects = ProjectService(self)
        self.costunits = CostUnitService(self)
        self.assigns = AssignService(self)
        self.times = TimeService(self)
        self.accounts = AccountService(self)

    def get_api_endpoint(self):
        """ returns the api end-point,respectively the url """
        return "https://api.smallinvoice.com/"

    def append_token_to_method(self, webservice_method):
        """appends the api-token to the webservice method, thus generating a valid url that can be requested. """
        return self.get_api_endpoint() + webservice_method + "/token/%s" % (
        self.api_token,)


    def request_with_method(self, method, data=None,
                            request_method=REQUEST_METHOD.AUTO):
        """ Excecutes the request with the specified method and returns either a raw or a parsed json object
        """
        url = self.append_token_to_method(method)
        if data:
            result = requests.post(url,
                                   data={ "data" : data.encode()},
                                   verify=False)
        else:
            if request_method == REQUEST_METHOD.POST:
                result = requests.post(url, verify=False)
            else:
                result = requests.get(url, verify=False)

        if result.status_code != requests.codes.ok:
            raise SmallInvoiceConnectionException(result.status_code,
                                                  result.text)
        else:
            #currently smallinvoice.ch sets text/html as default, not application/json
            content_type = result.headers.get('content-type')
            if 'text/html' in content_type or "application/json" in content_type:
                try:
                    data = json.loads(result.text)
                    if 'error' in data and data["error"] == True:
                        error_code = data['errorcode']
                        error_message = data['errormessage']
                        raise SmallInvoiceConnectionException(error_code,
                                                              error_message)
                    return data
                except ValueError:
                    raise SmallInvoiceConnectionException(
                        "could not parse result from smallinvoice", result.text)
            else:
                return result.content



