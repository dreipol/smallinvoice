__author__ = 'dreimac1'

all_cataloge_entries = "catalog/list"
catalog_entry_details = "catalog/get/id/%s"

class CatalogClient(object):

	def __init__(self, client):
		self.client  = client


	def all(self):
		""" returns all Catalog entries """
		return self.client.request_with_method(all_cataloge_entries)["items"]

	def details(self, catalog_id):
		""" returns the details to a specific catalog entry """
		return self.client.request_with_method(catalog_entry_details%(catalog_id,))["item"]