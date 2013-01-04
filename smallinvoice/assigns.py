from smallinvoice import REQUEST_METHOD, BaseJsonEncodableObject

__author__ = 'dreimac1'

assign_list = "assign/list"
assign_details = "assign/get/id/%s"
add_assign = "assign/add"
delete_assign = "assign/delete/id/%s"

class Assign(BaseJsonEncodableObject):

	def __init__(self, type, type_id, hours, date):
		self.type = type
		self.type_id = type_id
		self.hours = hours
		self.date = date


class AssignClient(object):

	def __init__(self, client):
		self.client  = client


	def all(self):
		""" returns all Assigns """
		return self.client.request_with_method(assign_list)["items"]

	def details(self, client_id):
		""" returns the details to a specific assign """
		return self.client.request_with_method(assign_details%(client_id,))["item"]

	def add(self, client):
		return self.client.request_with_method(add_assign, data=client)["id"]

	def delete(self, assign_id):
		return self.client.request_with_method(delete_assign%(assign_id,), request_method=REQUEST_METHOD.POST)