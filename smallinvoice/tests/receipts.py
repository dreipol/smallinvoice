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