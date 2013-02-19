from smallinvoice import PREVIEW_SIZE
from smallinvoice.client import *
from smallinvoice.letters import *
from smallinvoice.tests import TEST_API_TOKEN

def test_letters():
	client =  Client(TEST_API_TOKEN)
	result = client.letters.all()
	assert len(result) > 0

def test_letter_details():
	client =  Client(TEST_API_TOKEN)
	details = client.letters.details(32497)
	print details
	assert details["title"] == "Python-Update"

def test_letter_pdf():
	client =  Client(TEST_API_TOKEN)
	pdf = client.letters.pdf(32497)
	assert len(pdf)>0

def test_letter_preview():
	client =  Client(TEST_API_TOKEN)
	preview  = client.letters.preview(32497, 1, PREVIEW_SIZE.SMALL)
	assert len(preview)>0

def test_add_letter():

	l = Letter(client_id=24124, client_address_id=24183, date="2013-01-04", title="Python-Test")
	client = Client(TEST_API_TOKEN)
	all_clients = client.clients.all()
	for customer in all_clients:
		customer_details = client.clients.details(customer["id"])
		for address in customer_details["addresses"]:
			print "%s --> %s" % (customer["id"], address["id"],)
	letter_id = client.letters.add(l)
	details=client.letters.details(letter_id)
	assert details["title"] == "Python-Test"
	client.letters.delete(letter_id)

def test_update_letter():
	l = Letter(client_id=24124, client_address_id=24183, date="2013-01-04", title="Python-Update")
	l.id = 32497
	client =  Client(TEST_API_TOKEN)
	client.letters.update(l.id,l)
	details = client.letters.details(l.id)
	assert details["title"] == "Python-Update"

def test_email_letter():
	r = Recipient(cc=False, email="wild.etienne@gmail.com", name="Test Name")
	m = Mail(subject="Testsubject", body="Test email body", sendstatus=1, afterstatus=1, recipients=[r])
	m.id = 32497
	client = Client(TEST_API_TOKEN)
	client.letters.email(m.id, m)
	assert True

def test_status_letter():
	s = State(status=State.DRAFT)
	client = Client(TEST_API_TOKEN)
	client.letters.status(32497,status=s)
	assert client.letters.details(32497)["status"] == "7"