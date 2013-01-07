from smallinvoice import REQUEST_METHOD, BaseJsonEncodableObject

__author__ = 'dreimac1'

costunit_list = "costunit/list"
costunit_details = "costunit/get/id/%s"
add_costunit = "costunit/add"
delete_costunit = "costunit/delete/id/%s"
update_costunit = "costunit/edit/id/%s"

class Costunit(BaseJsonEncodableObject):

	def __init__(self, name, status):

		self.name = name
		self.status = status


class CostunitClient(object):

	def __init__(self, client):
		self.client  = client


	def all(self):
		""" returns all Costunits """
		return self.client.request_with_method(costunit_list)["items"]

	def details(self, client_id):
		""" returns the details to a specific costunit """
		return self.client.request_with_method(costunit_details%(client_id,))["item"]

	def add(self, client):
		return self.client.request_with_method(add_costunit, data=client)["id"]

	def delete(self, costunit_id):
		return self.client.request_with_method(delete_costunit%(costunit_id,), request_method=REQUEST_METHOD.POST)

	def update(self, costunit_id, costunit):
		return self.client.request_with_method(update_costunit%(costunit_id,), data=costunit)