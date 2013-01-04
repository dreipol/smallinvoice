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
	assert details["title"] == "dgdsfg"

def test_letter_pdf():
	client =  Client(TEST_API_TOKEN)
	pdf = client.letters.pdf(32497)
	assert len(pdf)>0

def test_letter_preview():
	client =  Client(TEST_API_TOKEN)
	preview  = client.letters.preview(32497, 1, PREVIEW_SIZE.SMALL)
	assert len(preview)>0

def test_add_letter():
	l = Letter(client_id=24401, client_address_id=24461, date="2013-01-04", title="Python-Test")
	client = Client(TEST_API_TOKEN)
	letter_id = client.letters.add(l)
	details=client.letters.details(letter_id)
	assert details["title"] == "Python-Test"
	client.letters.delete(letter_id)