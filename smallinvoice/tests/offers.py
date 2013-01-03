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