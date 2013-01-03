from smallinvoice.client import *
from smallinvoice.projets import *
from smallinvoice.tests import TEST_API_TOKEN

def test_get_all_projects():
	client = Client(TEST_API_TOKEN)
	result = client.projects.all()
	assert len(result)>0

def test_project_details():
	client =  Client(TEST_API_TOKEN)
	details = client.projects.details(545)
	assert details["estimate"] == "20"