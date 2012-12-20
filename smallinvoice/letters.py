__author__ = 'dreimac1'

letter_list = "letter/list"
letter_details = "letter/get/id/%s"
letter_pdf = "letter/pdf/id/%s"
letter_preview = "letter/preview/id/%s/page/%s/size/%s"


class LetterClient(object):
	""" This class wraps all letter related api
	"""
	def __init__(self, client):
		""" the LetterClient is only a wrapper of the real client, which must be passed in here"""
		self.client = client

	def all(self):
		""" returns all letters"""
		return self.client.request_with_method(letter_list)["items"]

	def details(self, letter_id):
		""" returns the details to a specific letter """
		return self.client.request_with_method(letter_details%(letter_id,))["item"]

	def pdf(self, letter_id):
		""" returns the pdf from the letter as binary data """
		return self.client.request_with_method(letter_pdf%(letter_id,))

	def preview(self, letter_id, page_number,size):
		""" returns a preview from the letter and the page with the specified size as binary data """
		return self.client.request_with_method(letter_preview%(letter_id, page_number,size,))