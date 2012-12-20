from smallinvoice import RESPONSE_TYPE

__author__ = 'dreimac1'

letter_list = "letter"
letter_details = "letter/id/%s"
letter_pdf = "letter/id/%s/type/pdf"
letter_preview = "letter/id/%s/type/preview/page/%s/size/%s"


class LetterClient(object):
	""" This class wraps all letter related api
	"""
	def __init__(self, client):
		""" the LetterClient is only a wrapper of the real client, which must be passed in here"""
		self.client = client

	def all(self):
		""" returns all letters"""
		return self.client.request_with_method(letter_list)

	def details(self, letter_id):
		""" returns the details to a specific letter """
		return self.client.request_with_method(letter_details%(letter_id,))

	def pdf(self, letter_id):
		""" returns the pdf from the letter as binary data """
		return self.client.request_with_method(letter_pdf%(letter_id,), type=RESPONSE_TYPE.RAW)

	def preview(self, letter_id, page_number,size):
		""" returns a preview from the letter and the page with the specified size as binary data """
		return self.client.request_with_method(letter_preview%(letter_id, page_number,size,), type=RESPONSE_TYPE.RAW)