from smallinvoice import SmallInvoiceConfigurationException, RESPONSE_TYPE, SmallInvoiceConnectionException
from smallinvoice.catalog import CatalogClient
from smallinvoice.customers import CustomerClient
from smallinvoice.letters import LetterClient
from smallinvoice.offers import OfferClient
from smallinvoice.receipts import ReceiptClient
from smallinvoice.unit_types import UnitTypeClient

__author__ = 'phil'
import requests
import json
from invoices import  InvoiceClient

class Client(object):
	""" A simple client wrapper for the smallinvoice.ch web service api"""
	country_code = None
	api_token = None

	def __init__(self,country_code,api_token):
		"""initializes the object, requires the country code and a valid api_token"""

		# raises an exception if the parameters are not correctly formatted.
		if not country_code or not api_token or len(country_code)<2:
			raise SmallInvoiceConfigurationException(self)
		self.country_code = country_code
		self.api_token = api_token

		self.invoices = InvoiceClient(self)
		self.clients = CustomerClient(self)
		self.offers = OfferClient(self)
		self.receipts = ReceiptClient(self)
		self.letters = LetterClient(self)
		self.catalog = CatalogClient(self)
		self.unittypes = UnitTypeClient(self)

	def get_api_endpoint(self):
		""" returns the api end-point,respectively the url with the correct subdomain """
		return "https://api-%s.smallinvoice.com/" % (self.country_code, )

	def append_token_to_method(self, webservice_method):
		"""appends the api-token to the webservice method, thus generating a valid url that can be requested. """
		return self.get_api_endpoint() + webservice_method + "/token/%s"%(self.api_token,)


	def request_with_method(self, method, type = RESPONSE_TYPE.JSON	):
		""" Excecutes the request with the specified method and returns a parsed json object
		"""
		url = self.append_token_to_method(method)
		result = requests.get(url)
		if result.status_code != requests.codes.ok:
			raise SmallInvoiceConnectionException(result.status_code, result.text)
		else:
			if type == RESPONSE_TYPE.JSON:
				return json.loads(result.text)
			else:
				return result.content
