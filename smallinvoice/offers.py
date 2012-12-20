__author__ = 'dreimac1'

offer_list = "offer/list"
offer_details = "offer/get/id/%s"
offer_pdf = "offer/pdf/id/%s"
offer_preview = "offer/preview/id/%s/page/%s/size/%s"


class OfferClient(object):
	""" This class wraps all offer related api
	"""
	def __init__(self, client):
		""" the OfferClient is only a wrapper of the real client, which must be passed in here"""
		self.client = client

	def all(self):
		""" returns all offers"""
		return self.client.request_with_method(offer_list)["items"]

	def details(self, offer_id):
		""" returns the details to a specific offer """
		return self.client.request_with_method(offer_details%(offer_id,))["item"]

	def pdf(self, offer_id):
		""" returns the pdf from the offer as binary data """
		return self.client.request_with_method(offer_pdf%(offer_id,))

	def preview(self, offer_id, page_number,size):
		""" returns a preview from the offer and the page with the specified size as binary data """
		return self.client.request_with_method(offer_preview%(offer_id, page_number,size,))
