# coding=utf-8
import json
import requests
from smallinvoice.commons import SmallInvoiceConfigurationException, SmallInvoiceConnectionException, REQUEST_METHOD
from smallinvoice.accounts import AccountService
from smallinvoice.assigns import AssignService
from smallinvoice.catalog import CatalogService
from smallinvoice.clients import ClientService
from smallinvoice.costunits import CostUnitService
from smallinvoice.invoices import InvoiceService
from smallinvoice.letters import LetterService
from smallinvoice.offers import OfferService
from smallinvoice.projects import ProjectService
from smallinvoice.receipts import ReceiptService
from smallinvoice.time import TimeService


class Smallinvoice(object):
    """ A simple client wrapper for the smallinvoice.ch web service api"""
    api_token = None
    services = {}

    @classmethod
    def register(cls, service):
        cls.services[service.name] = service

    def __init__(self, api_token):
        """initializes the object, requires the country code and a valid api_token"""

        # raises an exception if the parameters are not valid.
        if not api_token:
            raise SmallInvoiceConfigurationException(self)
        self.api_token = api_token

        for service_name, service_class in self.services.iteritems():
            setattr(self, '%ss' % service_name, service_class(self))

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
                                   data={"data": data.encode()},
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
                    if 'error' in data and data["error"] is True:
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


Smallinvoice.register(AccountService)
Smallinvoice.register(ClientService)
Smallinvoice.register(AssignService)
Smallinvoice.register(CatalogService)
Smallinvoice.register(CostUnitService)
Smallinvoice.register(InvoiceService)
Smallinvoice.register(LetterService)
Smallinvoice.register(OfferService)
Smallinvoice.register(ProjectService)
Smallinvoice.register(ReceiptService)
Smallinvoice.register(TimeService)