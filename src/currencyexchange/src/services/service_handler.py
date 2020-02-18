from urllib.request import urlopen, Request  # noqa: 401
from urllib.error import HTTPError  # noqa: 401
import json
import logging

logger = logging.getLogger(__name__)

BASE_URL_ENDPOINT = "https://api.exchangeratesapi.io/"
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


class ExtHTTPRestCallError(Exception):
    pass


def __call_ext_rest_endpoint(url):
    request = Request(url)
    try:
        response = urlopen(request)
    except HTTPError as httpex:
        raise ExtHTTPRestCallError(httpex.reason)

    data = json.loads(response.read())
    return data


def get_currency_exchange_rates(timeIndicator="latest"):
    currencyUrl = "{}{}".format(BASE_URL_ENDPOINT, timeIndicator)
    data = __call_ext_rest_endpoint(currencyUrl)
    return data


def get_currency_exchange_rate(
    countryCurrencyCode, baseCode="EUR", timeIndicator="latest"
):

    countryCurrencyCode = countryCurrencyCode.upper()
    baseCode = baseCode.upper()

    currencyUrl = "{}{}?base={}".format(BASE_URL_ENDPOINT, timeIndicator, baseCode)
    data = __call_ext_rest_endpoint(currencyUrl)

    return data["rates"][countryCurrencyCode]


def convert_currency(
    fromValue, fromCurrencyCode, toCurrencyCode, historicalDate="latest"
):
    exchangeRate = get_currency_exchange_rate(
        toCurrencyCode, fromCurrencyCode, historicalDate
    )

    return fromValue * exchangeRate
