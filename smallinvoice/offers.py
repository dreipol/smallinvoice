from smallinvoice import RESPONSE_TYPE

__author__ = 'dreimac1'

offer_list = "offer"
offer_details = "offer/id/%s"
offer_pdf = "offer/id/%s/type/pdf"
offer_preview = "offer/id/%s/type/preview/page/%s/size/%s"


class OfferClient(object):
	""" This class wraps all offer related api
	"""
	def __init__(self, client):
		""" the OfferClient is only a wrapper of the real client, which must be passed in here"""
		self.client = client

	def all(self):
		""" returns all offers"""
		return self.client.request_with_method(offer_list)

	def details(self, offer_id):
		""" returns the details to a specific offer """
		return self.client.request_with_method(offer_details%(offer_id,))

	def pdf(self, offer_id):
		""" returns the pdf from the offer as binary data """
		return self.client.request_with_method(offer_pdf%(offer_id,), type=RESPONSE_TYPE.RAW)

	def preview(self, offer_id, page_number,size):
		""" returns a preview from the offer and the page with the specified size as binary data """
		return self.client.request_with_method(offer_preview%(offer_id, page_number,size,), type=RESPONSE_TYPE.RAW)
