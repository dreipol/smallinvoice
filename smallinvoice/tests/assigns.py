from smallinvoice.client import *
from smallinvoice.assigns import *
from smallinvoice.tests import TEST_API_TOKEN

def test_get_all_assigns():
	client = Client(TEST_API_TOKEN)
	result = client.assigns.all()
	assert len(result)>0

def test_assigns_details():
	client =  Client(TEST_API_TOKEN)
	details = client.assigns.details(12542)
	assert details["employee"] == "Andreas Graf"