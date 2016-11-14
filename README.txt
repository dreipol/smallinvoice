===========
smallinvoice api wrapper
===========

This python package is a wrapper for the web service api of http://www.smallinvoice.ch, an elegant online invoicing and
project management service. For more information about the API consult: http://developer.smallinvoice.com/


Implemented Services
=========

The following services are completely wrapped

* Invoices

* Clients

* Offers

* Assigns

* Catalog

* Projects

* Times

* Costunits

* Receipts

* Accounts

* Client Accounts


Usage
=========

from smallinvoice import Smallinvoice

smallinvoice = Smallinvoice(YOUR_API_TOKEN)
smallinvoice.clients.all()
