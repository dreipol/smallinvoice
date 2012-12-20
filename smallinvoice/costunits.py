__author__ = 'dreimac1'

costunit_list = "costunit/list"
costunit_details = "costunit/get/id/%s"

class CostunitClient(object):

	def __init__(self, client):
		self.client  = client


	def all(self):
		""" returns all Costunits """
		return self.client.request_with_method(costunit_list)["items"]

	def details(self, client_id):
		""" returns the details to a specific costunit """
		return self.client.request_with_method(costunit_details%(client_id,))["item"]