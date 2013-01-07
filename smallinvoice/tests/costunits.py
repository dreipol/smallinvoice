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

def test_add_costunit():
	c = Costunit(name="Testunit", status=1)
	client = Client(TEST_API_TOKEN)
	costunit_id = client.costunits.add(c)
	details=client.costunits.details(costunit_id)
	assert details["name"] == "Testunit"
	client.costunits.delete(costunit_id)

def test_update_costunit():
	c = Costunit(name="Kostenstellentest", status=1)
	c.id = 234
	client =  Client(TEST_API_TOKEN)
	client.costunits.update(c.id,c)
	details = client.costunits.details(c.id)
	assert details["name"] == "Kostenstellentest"