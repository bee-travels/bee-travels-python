import pytest
from src.services.service_handler import convert_currency, get_currency_exchange_rates


@pytest.mark.xfail(raises=AssertionError)
def test_convert_currency():
    """ this test must mostly fail, unless exchange rates for the day are exact
    as of the day (Sunday Feb 16th 2020) when this test did work or the internet or external service was/is unavailable!"""
    countryCurrencyCode = "USD"
    expected = 13.247555801999999

    actual = convert_currency(10, countryCurrencyCode, "CAD")
    assert actual == expected


@pytest.mark.xfail(raises=Exception)
def test_get_exchange_rates():
    expected = {}
    actual = get_currency_exchange_rates()
    assert actual == expected
