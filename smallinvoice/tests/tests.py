from smallinvoice.customers import Address, Customer, CUSTOMER_TYPE, CUSTOMER_GENDER
from smallinvoice.invoices import Position, Invoice
from smallinvoice.tests import TEST_API_TOKEN

__author__ = 'phil'
from smallinvoice import PREVIEW_SIZE



from smallinvoice.client import Client, SmallInvoiceConfigurationException, SmallInvoiceConnectionException


def client_configuration_no_token_test():
	try:
		client = Client(None)
		client.get_api_endpoint()
		assert False
	except SmallInvoiceConfigurationException:
		assert True

def get_api_endpoint_test():
	client = Client("test")
	assert client.get_api_endpoint() == "https://api.smallinvoice.com/"

def test_append_token_to_endpoint():
	client = Client( "test-token")
	result = client.append_token_to_method("test_method")
	assert result == "https://api.smallinvoice.com/test_method/token/test-token"


def test_authentication_error():
	client = Client("playgroundclienttests")
	try:
		client.invoices.all()
		assert False
	except SmallInvoiceConnectionException, e:
		assert True
