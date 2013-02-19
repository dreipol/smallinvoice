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

def test_add_time():
	t = Time(start="0900", end="1200", date="2013-01-03")
	client = Client(TEST_API_TOKEN)
	time_id = client.times.add(t)
	details=client.times.details(time_id)
	assert details["start"] == "0900"
	client.times.delete(time_id)

def test_update_time():
	t = Time(start="0900", end="1200", date="2013-01-03")
	t.id = 7706
	client =  Client(TEST_API_TOKEN)
	client.times.update(t.id,t)
	details = client.times.details(t.id)
	assert details["start"] == "0900"