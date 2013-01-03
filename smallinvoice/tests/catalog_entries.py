from smallinvoice.client import *
from smallinvoice.catalog import *
from smallinvoice.tests import TEST_API_TOKEN

def test_get_all_catalog_entries():
	client = Client(TEST_API_TOKEN)
	result = client.catalog.all()
	assert len(result)>0

def test_catalog_entry_details():
	client =  Client(TEST_API_TOKEN)
	details = client.catalog.details(1696)
	assert details["name"] == "Halbe Tage ohne Essen"