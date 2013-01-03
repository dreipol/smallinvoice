from smallinvoice.client import *
from smallinvoice.time import *
from smallinvoice.tests import TEST_API_TOKEN

def test_get_all_times():
	client = Client(TEST_API_TOKEN)
	result = client.times.all()
	assert len(result)>0

def test_times_details():
	client =  Client(TEST_API_TOKEN)
	details = client.times.details(7706)
	assert details["start"] == "0900"