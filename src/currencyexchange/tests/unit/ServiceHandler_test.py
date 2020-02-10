from src.services.serviceHandler import convertCurrency

# def test_convertCurrency(mocked_urllib):
#     """ test the currency conversion against a mock """


#     expected_ =    {"result":11.058}
#     actual_ = convertCurrency(10,'EUR','USD','latest')
#     assert actual_ == expected_


def test_convertCurrency():
    countryCurrencyCode_ = "USD"
    expected_ = 13.313884584

    actual_ = convertCurrency(10, countryCurrencyCode_, "CAD")
    assert actual_ == expected_
