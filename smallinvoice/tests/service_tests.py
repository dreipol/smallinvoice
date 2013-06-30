# coding=utf-8
from smallinvoice import Smallinvoice, SmallInvoiceConnectionException, SmallInvoiceConfigurationException


def client_configuration_no_token_test():
    try:
        client = Smallinvoice(None)
        client.get_api_endpoint()
        assert False
    except SmallInvoiceConfigurationException:
        assert True


def get_api_endpoint_test():
    client = Smallinvoice("test")
    assert client.get_api_endpoint() == "https://api.smallinvoice.com/"


def test_append_token_to_endpoint():
    client = Smallinvoice("test-token")
    result = client.append_token_to_method("test_method")
    assert result == "https://api.smallinvoice.com/test_method/token/test-token"


def test_authentication_error():
    client = Smallinvoice("playgroundclienttests")
    try:
        client.invoices.all()
        assert False
    except SmallInvoiceConnectionException:
        assert True
