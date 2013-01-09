from smallinvoice import PREVIEW_SIZE
from smallinvoice.client import *
from smallinvoice.receipts import *
from smallinvoice.tests import TEST_API_TOKEN

def test_receipts():
	client =  Client(TEST_API_TOKEN)
	result = client.receipts.all()
	assert len(result) > 0

def test_receipt_details():
	client =  Client(TEST_API_TOKEN)
	details = client.receipts.details(44714)
	assert details["totalamount"] == "2430"

def test_receipt_pdf():
	client =  Client(TEST_API_TOKEN)
	pdf = client.receipts.pdf(44714)
	assert len(pdf)>0

def test_receipt_preview():
	client =  Client(TEST_API_TOKEN)
	preview  = client.receipts.preview(44714, 1, PREVIEW_SIZE.SMALL)
	assert len(preview)>0

def test_add_receipt():
	p = Position(type=1, number=2, name="Basisbeitrag", description="Test", cost=6000, unit=3, amount=1)
	r = Receipt(client_id=24401, client_address_id=24461, currency="CHF", date="2013-01-03", language="de", positions=[p])
	client = Client(TEST_API_TOKEN)
	receipt_id = client.receipts.add(r)
	details=client.receipts.details(receipt_id)

	the_position = details["positions"][0]
	assert the_position["description"] == "Test"
	client.receipts.delete(receipt_id)

def test_update_receipt():
	p = Position(type=1, number=2, name="Basisbeitrag", description="Update", cost=2430, unit=3, amount=1)
	p.id = 51090
	r = Receipt(client_id=24401, client_address_id=24461, currency="CHF", date="2013-01-03", language="de", positions=[p])
	r.id = 44714
	client =  Client(TEST_API_TOKEN)
	client.receipts.update(r.id,r)
	details = client.receipts.details(r.id)
	the_position = details["positions"][0]
	assert the_position["description"] == "Update"

def test_email_receipt():
	r = Recipient(cc=False, email="wild.etienne@gmail.com", name="Test Name")
	m = Mail(subject="Testsubject", body="Test email body", sendstatus=1, afterstatus=1, recipients=[r])
	m.id = 44714
	client = Client(TEST_API_TOKEN)
	client.receipts.email(m.id, m)
	assert True

def test_status_receipt():
	s = State(status=State.PAID)
	client = Client(TEST_API_TOKEN)
	client.receipts.status(44714,status=s)
	assert client.receipts.details(44714)["status"] == "10"