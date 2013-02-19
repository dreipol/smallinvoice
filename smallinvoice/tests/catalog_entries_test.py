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
	c = Catalog(type=1, unit=2, name="Add_Test", cost_per_unit=50)
	client = Client(TEST_API_TOKEN)
	catalog_id = client.catalog.add(c)
	details=client.catalog.details(catalog_id)
	assert details["name"] == "Add_Test"
	client.catalog.delete(catalog_id)

def test_update_catalog():
	c = Catalog(type=1, unit=2, name="Update", cost_per_unit=50)
	c.id = 178187
	client =  Client(TEST_API_TOKEN)
	client.catalog.update(c.id,c)
	details = client.catalog.details(c.id)
	assert details["name"] == "Update"