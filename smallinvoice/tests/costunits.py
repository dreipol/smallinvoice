from smallinvoice.client import *
from smallinvoice.costunits import *
from smallinvoice.tests import TEST_API_TOKEN

def test_get_all_costunits():
	client = Client(TEST_API_TOKEN)
	result = client.costunits.all()
	assert len(result)>0

def test_costunits_details():
	client =  Client(TEST_API_TOKEN)
	details = client.costunits.details(234)
	assert details["name"] == "Kostenstellentest"