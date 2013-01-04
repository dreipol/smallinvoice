from smallinvoice.client import *
from smallinvoice.customers import *
from smallinvoice.tests import TEST_API_TOKEN

def test_get_all_clients():
	client = Client(TEST_API_TOKEN)
	result = client.clients.all()
	print(result)
	assert len(result)>0

def test_client_details():
	client =  Client(TEST_API_TOKEN)
	details = client.clients.details(24401)
	assert details["addition"] == "Andreas Graf"


def test_add_address():
	a = Address(primary=1, street="Kernstrasse", streetno="60", city="Zurich", code="8004", country="CH")
	c = Customer(type=CUSTOMER_TYPE.PRIVATE, gender=CUSTOMER_GENDER.MALE, name="Hans Muster", language="DE", addresses=[a])
	client = Client(TEST_API_TOKEN)
	client_id = client.clients.add(c)
	details=client.clients.details(client_id)
	assert details["name"] == "Hans Muster"
	client.clients.delete(client_id)