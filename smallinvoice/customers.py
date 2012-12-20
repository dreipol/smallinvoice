__author__ = 'dreimac1'

all_clients = "client/list"
client_details = "client/get/id/%s"

class CustomerClient(object):

	def __init__(self, client):
		self.client  = client


	def all(self):
		""" returns all Clients """
		return self.client.request_with_method(all_clients)["items"]

	def details(self, client_id):
		""" returns the details to a specific client """
		return self.client.request_with_method(client_details%(client_id,))["item"]