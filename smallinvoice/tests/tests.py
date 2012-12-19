__author__ = 'phil'
from smallinvoice import PREVIEW_SIZE

TEST_API_TOKEN = ""

from smallinvoice.client import Client, SmallInvoiceConfigurationException, SmallInvoiceConnectionException

def client_configuration_wrong_country_code_test():
	try:
		client = Client("a","a")
		client.get_api_endpoint()
		assert False
	except SmallInvoiceConfigurationException:
		assert True

def client_configuration_no_country_code_test():
	try:
		client = Client(None,"a")
		client.get_api_endpoint()
		assert False
	except SmallInvoiceConfigurationException:
		assert True

def client_configuration_no_token_test():
	try:
		client = Client("aa",None)
		client.get_api_endpoint()
		assert False
	except SmallInvoiceConfigurationException:
		assert True

def get_api_endpoint_test():
	client = Client("ch", "test")
	assert client.get_api_endpoint() == "https://api-ch.smallinvoice.com/"

	client = Client("uk", "test")
	assert client.get_api_endpoint() == "https://api-uk.smallinvoice.com/"

def test_append_token_to_endpoint():
	client = Client("ch", "test-token")
	result = client.append_token_to_method("test_method")
	assert result == "https://api-ch.smallinvoice.com/test_method/token/test-token"


def test_authentication_error():
	client = Client("ch", "playgroundclienttests")
	try:
		client.invoices.all()
		assert False
	except SmallInvoiceConnectionException, e:
		print e.message
		assert True

def test_invoices():
	client =  Client("ch", TEST_API_TOKEN)
	invoices = client.invoices.all()
	assert len(invoices) > 0

def test_invoice_details():
	client =  Client("ch", TEST_API_TOKEN)
	details = client.invoices.details(25676)
	assert details["totalamount"] == "1440"

def test_invoice_pdf():
	client =  Client("ch", TEST_API_TOKEN)
	pdf = client.invoices.pdf(25676)
	assert len(pdf)>0

def test_invoice_preview():
	client =  Client("ch", TEST_API_TOKEN)
	preview  = client.invoices.preview(25676, 1, PREVIEW_SIZE.SMALL)
	#f = open("/Users/phil/test2.jpg", "wb")
	#f.write(preview)
	#f.close()
	assert len(preview)>0


