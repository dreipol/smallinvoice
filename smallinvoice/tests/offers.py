from smallinvoice import PREVIEW_SIZE
from smallinvoice.client import *
from smallinvoice.offers import *
from smallinvoice.tests import TEST_API_TOKEN

def test_offers():
	client =  Client(TEST_API_TOKEN)
	result = client.offers.all()
	assert len(result) > 0

def test_offer_details():
	client =  Client(TEST_API_TOKEN)
	details = client.offers.details(26193)
	assert details["totalamount"] == "1350"

def test_offer_pdf():
	client =  Client(TEST_API_TOKEN)
	pdf = client.offers.pdf(26193)
	assert len(pdf)>0

def test_offer_preview():
	client =  Client(TEST_API_TOKEN)
	preview  = client.offers.preview(26193, 1, PREVIEW_SIZE.SMALL)
	assert len(preview)>0

def test_add_offer():
	p = Position(type=1, number=2, name="Basisbeitrag", description="Test", cost=6000, unit=3, amount=1)
	o = Offer(client_id=24401, client_address_id=24461, currency="CHF", date="2013-01-03", due="2013-01-24", language="de", positions=[p])
	client = Client(TEST_API_TOKEN)
	offer_id = client.offers.add(o)
	details=client.offers.details(offer_id)

	the_position = details["positions"][0]
	assert the_position["description"] == "Test"
	client.offers.delete(offer_id)

def test_update_offer():
	p = Position(type=1, number=2, name="Basisbeitrag", description="Update", cost=1350, unit=3, amount=1)
	p.id = 51090
	o = Offer(client_id=24401, client_address_id=24461, currency="CHF", date="2013-01-03", due="2013-01-24", language="de", positions=[p])
	o.id = 26193
	client =  Client(TEST_API_TOKEN)
	client.offers.update(o.id,o)
	details = client.offers.details(o.id)
	the_position = details["positions"][0]
	assert the_position["description"] == "Update"

def test_email_offer():
	r = Recipient(cc=False, email="wild.etienne@gmail.com", name="Test Name")
	m = Mail(subject="Testsubject", body="Test email body", sendstatus=1, afterstatus=1, recipients=[r])
	m.id = 26193
	client = Client(TEST_API_TOKEN)
	client.offers.email(m.id, m)
	assert True

def test_status_invoice():
	s = State(status=State.OK)
	client = Client(TEST_API_TOKEN)
	client.offers.status(26193,status=s)
	assert client.offers.details(26193)["status"] == "9"