import pytest
from src.services import countryCurrencyCodeHandler
from src.errors.UserDefinedErrors import NotFoundError


def test_GetCurrencyNameAndCodeForRealCountry():
    expected_ = {
        "country": "South Africa",
        "currencyName": "South African rand",
        "currencyCode": "ZAR",
    }
    actual_ = countryCurrencyCodeHandler.getCurrencyNameAndCode("South Africa")
    assert actual_ == expected_


def test_CSV_to_Dict():
    """ we need a test to confirm we can read a csv and translate it into a useful python structure
    in this case a list of dict rows"""
    expected_ = {
        "country": "Zimbabwe",
        "currencyCode": "USD",
        "currencyName": "United States dollar",
    }

    actual_ = countryCurrencyCodeHandler.readData()
    assert actual_[-1] == expected_
    assert len(actual_) == 253


def test_GetCurrencyNameAndCodeForNoCountry():
    with pytest.raises(NotFoundError):
        countryCurrencyCodeHandler.getCurrencyNameAndCode("Westeros")


# there are 2 other ways to handle exceptions in pytest

# first test the error message is as expected
def test_GetCurrencyNameAndCodeForNoCountryMessage():
    try:
        countryCurrencyCodeHandler.getCurrencyNameAndCode("Westeros")
    except NotFoundError as nfex:
        assert nfex.message == "country Westeros does not exist"


# can mark a test with a python decorator that it will fail but that's OK it does as it should
@pytest.mark.xfail(raises=NotFoundError)
def test_GetCurrencyNameAndCodeForNoCountryWithXfailMark():
    countryCurrencyCodeHandler.getCurrencyNameAndCode("Westeros")
