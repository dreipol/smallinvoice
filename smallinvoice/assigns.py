__author__ = 'dreimac1'

assign_list = "assign/list"
assign_details = "assign/get/id/%s"

class AssignClient(object):

	def __init__(self, client):
		self.client  = client


	def all(self):
		""" returns all Assigns """
		return self.client.request_with_method(assign_list)["items"]

	def details(self, client_id):
		""" returns the details to a specific assign """
		return self.client.request_with_method(assign_details%(client_id,))["item"]