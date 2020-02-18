from src.services import countryCurrencyCodeHandler
import pytest

def test_get_currency_name_y_code_for_real():
    expected_ = {
        "country": "South Africa",
        "currencyName": "South African rand",
        "currencyCode": "ZAR",
    }
    actual_ = countryCurrencyCodeHandler.get_currency_name_and_code("South Africa")
    assert actual_ == expected_


def test_get_single_for_real_currencycode():
    currencyCode_ = "ZAR"
    expectedCountries_ = [
        "South Africa",
    ]

    expected_ = {
        "currencyCode": "ZAR",
        "currencyName": "South African rand",
        "country": expectedCountries_,
    }
    actual_ = countryCurrencyCodeHandler.get_country_and_currency_code(currencyCode_)
    assert actual_ == expected_

def test_get_fictional_currencycode():
    currencyCode_ = "ZZZ"
    with pytest.raises(countryCurrencyCodeHandler.NotFoundError):
        countryCurrencyCodeHandler.get_country_and_currency_code(currencyCode_)

def test_get_invalid_currencycode():
    currencyCode_ = "ZZZZXXX"
    with pytest.raises(countryCurrencyCodeHandler.InvalidCountryCode):
        countryCurrencyCodeHandler.get_country_and_currency_code(currencyCode_)

    
def test_get_multiple_countries_for_real_currencycode():
    currencyCode_ = "USD"
    expected_ = {
        "currencyCode": "USD",
        "currencyName": "United States dollar",
        "country": __get_expected_countries(),
    }
    actual_ = countryCurrencyCodeHandler.get_country_and_currency_code(currencyCode_)
    assert actual_ == expected_


def test_csv_to_dict():
    """ we need a test to confirm we can read a csv and translate it into a useful python structure
    in this case a list of dict rows"""
    expected_ = {
        "country": "Zimbabwe",
        "currencyCode": "USD",
        "currencyName": "United States dollar",
    }

    actual_ = countryCurrencyCodeHandler.read_data()
    assert actual_[-1] == expected_
    assert len(actual_) == 253


def test_get_currency_name_y_code_for_fictional_country():
    with pytest.raises(countryCurrencyCodeHandler.NotFoundError):
        countryCurrencyCodeHandler.get_currency_name_and_code("Westeros")

# can mark alternatively test with a python decorator 
# that it will fail but that's OK it does as it should
@pytest.mark.xfail(raises=countryCurrencyCodeHandler.NotFoundError)
def test_get_currency_name_y_code_for_fictional_country_xfail_example():
    countryCurrencyCodeHandler.get_currency_name_and_code("Westeros")


def __get_expected_countries():
    return [
        "American Samoa",
        "Bonaire",
        "British Indian Ocean Territory",
        "British Virgin Islands",
        "Caribbean Netherlands",
        "Ecuador",
        "El Salvador",
        "Guam",
        "Marshall Islands",
        "Micronesia",
        "Northern Mariana Islands",
        "Palau",
        "Panama",
        "Puerto Rico",
        "Saba",
        "Sint Eustatius",
        "Timor-Leste",
        "Turks and Caicos Islands",
        "United States of America",
        "US Virgin Islands",
        "Wake Island",
        "Zimbabwe",
    ]