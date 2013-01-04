from smallinvoice import PREVIEW_SIZE
from smallinvoice.client import *
from smallinvoice.invoices import *
from smallinvoice.tests import TEST_API_TOKEN

def test_invoices():
	client =  Client(TEST_API_TOKEN)
	invoices = client.invoices.all()
	assert len(invoices) > 0

def test_invoice_details():
	client =  Client(TEST_API_TOKEN)
	details = client.invoices.details(25676)
	print details
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

def test_add_invoice():
	p = Position(type=1, number=2, name="Basisbeitrag", description="Test", cost=6000, unit=3, amount=1)
	i = Invoice(client_id=24401, client_address_id=24461, currency="CHF", date="2013-01-03", due="2013-01-24", language="de", positions=[p])
	client = Client(TEST_API_TOKEN)
	invoice_id = client.invoices.add(i)
	details=client.invoices.details(invoice_id)

	the_position = details["positions"][0]
	assert the_position["name"] == "Basisbeitrag"
	client.invoices.delete(invoice_id)