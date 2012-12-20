__author__ = 'dreimac1'

all_unit_types = "unittype"

class UnitTypeClient(object):

	def __init__(self, client):
		""" the UnitTypeClient is only a wrapper of the real client, which must be passed in here"""
		self.client  = client


	def all(self):
		""" returns all Unit Types """
		return self.client.request_with_method(all_unit_types)