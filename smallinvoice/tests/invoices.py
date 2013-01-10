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
	assert details["totalamount"] == "1440"

def test_invoice_pdf():
	client =  Client(TEST_API_TOKEN)
	pdf = client.invoices.pdf(25676)
	assert len(pdf)>0

def test_invoice_preview():
	client =  Client(TEST_API_TOKEN)
	preview  = client.invoices.preview(25676, 1, PREVIEW_SIZE.SMALL)
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

def test_update_invoice():
	p = Position(type=1, number=2, name="Basisbeitrag", description="Update", cost=1440, unit=3, amount=1)
	p.id = 51090
	i = Invoice(client_id=24401, client_address_id=24461, currency="CHF", date="2013-01-03", due="2013-01-24", language="de", positions=[p])
	i.id = 25676
	client =  Client(TEST_API_TOKEN)
	client.invoices.update(i.id,i)
	details = client.invoices.details(i.id)
	the_position = details["positions"][0]
	assert the_position["description"] == "Update"

def test_email_invoice():
	r = Recipient(cc=False, email="wild.etienne@gmail.com", name="Test Name")
	m = Mail(subject="Testsubject", body="Test email body", sendstatus=1, afterstatus=1, recipients=[r])
	m.id = 25676
	client = Client(TEST_API_TOKEN)
	client.invoices.email(m.id, m)
	assert True

def test_status_invoice():
	s = State(status=State.REMINDER)
	client = Client(TEST_API_TOKEN)
	client.invoices.status(25676,status=s)
	assert client.invoices.details(25676)["status"] == "3"

def test_invoice_payment():
	p = Payment(amount=140, date="2013-09-01", type=1, keep_status=0)
	print p
	client = Client(TEST_API_TOKEN)
	client.invoices.payment(25767, p)
	assert client.invoices.details(25767)["date"] == "2013-09-01"
