__author__ = 'phil'
from smallinvoice import PREVIEW_SIZE

TEST_API_TOKEN = "aaac7f912ad6eb47ac13ec9b32a15d09"

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

def test_invoices():
	client =  Client(TEST_API_TOKEN)
	invoices = client.invoices.all()
	assert len(invoices) > 0

def test_invoice_details():
	client =  Client(TEST_API_TOKEN)
	details = client.invoices.details(25676)
	assert details["totalamount"] == "1440"

def test_invoice_pdf():
	client =  Client(TEST_API_TOKEN)
	pdf = client.invoices.pdf(25676)
	assert len(pdf)>0

def test_invoice_preview():
	client =  Client(TEST_API_TOKEN)
	preview  = client.invoices.preview(25676, 1, PREVIEW_SIZE.SMALL)
	#f = open("/Users/phil/test2.jpg", "wb")
	#f.write(preview)
	#f.close()
	assert len(preview)>0

def test_get_all_clients():
	client = Client(TEST_API_TOKEN)
	result = client.clients.all()
	assert len(result)>0

#def test_client_details():
#	client =  Client(TEST_API_TOKEN)
#	details = client.clients.details(1001)
#	assert details["name"] == "Mutter"

def test_offers():
	client =  Client(TEST_API_TOKEN)
	result = client.offers.all()
	assert len(result) == 0

#def test_offer_details():
#	client =  Client(TEST_API_TOKEN)
#	details = client.offers.details(1)
#	assert details["totalamount"] > "0"

#def test_offer_pdf():
#	client =  Client(TEST_API_TOKEN)
#	pdf = client.offers.pdf(1)
#	assert len(pdf)>0

#def test_offer_preview():
#	client =  Client(TEST_API_TOKEN)
#	preview  = client.offers.preview(1, 1, PREVIEW_SIZE.SMALL)
#	assert len(preview)>0

def test_receipts():
	client =  Client(TEST_API_TOKEN)
	result = client.receipts.all()
	assert len(result) == 0

#def test_receipt_details():
#	client =  Client(TEST_API_TOKEN)
#	details = client.receipts.details(1)
#	assert details["totalamount"] > "0"

#def test_receipt_pdf():
#	client =  Client(TEST_API_TOKEN)
#	pdf = client.receipts.pdf(1)
#	assert len(pdf)>0

#def test_receipt_preview():
#	client =  Client(TEST_API_TOKEN)
#	preview  = client.receipts.preview(1, 1, PREVIEW_SIZE.SMALL)
#	assert len(preview)>0

def test_letters():
	client =  Client(TEST_API_TOKEN)
	result = client.letters.all()
	assert len(result) == 0

#def test_letter_details():
#	client =  Client(TEST_API_TOKEN)
#	details = client.letters.details(1)
#	assert details["totalamount"] > "0"

#def test_letter_pdf():
#	client =  Client(TEST_API_TOKEN)
#	pdf = client.letters.pdf(1)
#	assert len(pdf)>0

#def test_letter_preview():
#	client =  Client(TEST_API_TOKEN)
#	preview  = client.letters.preview(1, 1, PREVIEW_SIZE.SMALL)
#	assert len(preview)>0

def test_get_all_catalog_entries():
	client = Client(TEST_API_TOKEN)
	result = client.catalog.all()
	assert len(result)>0

#def test_catalog_entry_details():
#	client =  Client(TEST_API_TOKEN)
#	details = client.catalog.details(1)
#	assert details["totalamount"] > "0"

def test_get_all_projects():
	client = Client(TEST_API_TOKEN)
	result = client.projects.all()
	assert len(result)==0

#def test_project_details():
#	client =  Client(TEST_API_TOKEN)
#	details = client.projects.details(1)
#	assert details["totalamount"] > "0"

def test_get_all_costunits():
	client = Client(TEST_API_TOKEN)
	result = client.costunits.all()
	assert len(result)==0

#def test_costunits_details():
#	client =  Client(TEST_API_TOKEN)
#	details = client.costunits.details(1)
#	assert details["totalamount"] > "0"

def test_get_all_assigns():
	client = Client(TEST_API_TOKEN)
	result = client.assigns.all()
	assert len(result)==0

#def test_assigns_details():
#	client =  Client(TEST_API_TOKEN)
#	details = client.assigns.details(1)
#	assert details["totalamount"] > "0"

def test_get_all_times():
	client = Client(TEST_API_TOKEN)
	result = client.times.all()
	assert len(result)==0

#def test_times_details():
#	client =  Client(TEST_API_TOKEN)
#	details = client.times.details(1)
#	assert details["totalamount"] > "0"