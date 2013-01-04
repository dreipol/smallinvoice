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

def test_add_assign():
	a = Assign(type=1, type_id=2, hours="8.00", date="2013-01-03")
	client = Client(TEST_API_TOKEN)
	assign_id = client.assigns.add(a)
	details=client.assigns.details(assign_id)
	assert details["date"] == "2013-01-03"
	client.assigns.delete(assign_id)