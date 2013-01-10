from smallinvoice import SmallInvoiceConfigurationException, SmallInvoiceConnectionException, BaseJsonEncodableObject, REQUEST_METHOD
from smallinvoice.assigns import AssignClient
from smallinvoice.catalog import CatalogClient
from smallinvoice.costunits import CostunitClient
from smallinvoice.customers import CustomerClient
from smallinvoice.letters import LetterClient
from smallinvoice.offers import OfferClient
from smallinvoice.projects import ProjectClient
from smallinvoice.receipts import ReceiptClient
from smallinvoice.time import TimeClient

__author__ = 'phil'
import requests
import json
from invoices import  InvoiceClient

class Client(object):
	""" A simple client wrapper for the smallinvoice.ch web service api"""
	country_code = None
	api_token = None

	def __init__(self,api_token):
		"""initializes the object, requires the country code and a valid api_token"""

		# raises an exception if the parameters are not valid.
		if not api_token :
			raise SmallInvoiceConfigurationException(self)
		self.api_token = api_token

		self.invoices = InvoiceClient(self)
		self.clients = CustomerClient(self)
		self.offers = OfferClient(self)
		self.receipts = ReceiptClient(self)
		self.letters = LetterClient(self)
		self.catalog = CatalogClient(self)
		self.projects = ProjectClient(self)
		self.costunits = CostunitClient(self)
		self.assigns = AssignClient(self)
		self.times = TimeClient(self)

	def get_api_endpoint(self):
		""" returns the api end-point,respectively the url """
		return "https://api.smallinvoice.com/"

	def append_token_to_method(self, webservice_method):
		"""appends the api-token to the webservice method, thus generating a valid url that can be requested. """
		return self.get_api_endpoint() + webservice_method + "/token/%s"%(self.api_token,)


	def request_with_method(self, method, data=None, request_method=REQUEST_METHOD.AUTO):
		""" Excecutes the request with the specified method and returns either a raw or a parsed json object
		"""
		url = self.append_token_to_method(method)
		if data:
			print data.encode()
			result = requests.post(url,data={"data":data.encode()}, verify=False)
		else:
			if request_method == REQUEST_METHOD.POST:
				result = requests.post(url,verify=False)
			else:
				result = requests.get(url,verify=False)

		if result.status_code != requests.codes.ok:
			raise SmallInvoiceConnectionException(result.status_code, result.text)
		else:
			#currently smallinvoice.ch sets text/html as default, not application/json
			content_type = result.headers.get('content-type')
			if 'text/html' in content_type or "application/json" in content_type:
				try:
					data = json.loads(result.text)
					if 'error' in data and data["error"]==True:
						error_code = data['errorcode']
						error_message = data['errormessage']
						raise SmallInvoiceConnectionException(error_code, error_message)
					return data
				except ValueError:
					raise SmallInvoiceConnectionException("could not parse result from smallinvoice", result.text)
			else:
				return result.content
