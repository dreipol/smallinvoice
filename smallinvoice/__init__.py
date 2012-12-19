__author__ = 'phil'
class RESPONSE_TYPE:
	JSON = 1
	RAW = 2

class PREVIEW_SIZE:
	SMALL = 240
	MEDIUM = 595
	BIG = 1240

class SmallInvoiceException(Exception):
	""" Base class for all exceptions raised by smallinvoice """
	def __init__(self, message):
		final_message = "smallinvoice-client exception: %s" % (message)
		super(Exception, self).__init__(final_message)

class SmallInvoiceConfigurationException(SmallInvoiceException):
	""" Thrown when the client is not properl configurated"""
	def __init__(self, client):
		message = "Wrong configuration.: "\
				  "token: %s" % (client.api_token,)
		super(SmallInvoiceException, self).__init__(message)

class SmallInvoiceConnectionException(SmallInvoiceException):
	""" The client could not connect for any reason. """
	def __init__(self, status_code, remote_message):
		message = "Failed to Connect, Status %s; Message: %s" % (status_code, remote_message)
		super(SmallInvoiceException, self).__init__(message)

