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

def test_add_catalog():
	c = Catalog(type=1, unit=2, name="Pythontest", cost_per_unit=50)
	client = Client(TEST_API_TOKEN)
	catalog_id = client.catalog.add(c)
	details=client.catalog.details(catalog_id)
	assert details["name"] == "Pythontest"
	client.catalog.delete(catalog_id)