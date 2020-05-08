from urllib.request import urlopen, Request  # noqa: 401
from urllib.error import HTTPError  # noqa: 401
import json
import logging
import os
import pdb

logger = logging.getLogger(__name__)

BASE_URL_ENDPOINT = os.environ.get("BASE_URL_ENDPOINT")
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


class NotFoundException(Exception):
    pass


def __callExtRestEndPoint(url):
    logger.warn(url)
    request = Request(url)
    try:
        response = urlopen(request)
    except HTTPError as httpex:
        raise NotFoundException(httpex.reason)

    data = json.loads(response.read())
    return data


def getCurrencyExchangeRates(timeIndicator="latest"):
    currencyUrl = "{}{}".format(BASE_URL_ENDPOINT, timeIndicator)
    data = __callExtRestEndPoint(currencyUrl)
    return data


def getCurrencyExchangeRates2(countryCurrencyCode, baseCode='EUR', timeIndicator='latest'):
    countryCurrencyCode = countryCurrencyCode.upper()
    baseCode = baseCode.upper()

    currencyUrl = "{}{}?base={}".format(BASE_URL_ENDPOINT, timeIndicator, baseCode)
    #logger.warn(currencyUrl)
    data = __callExtRestEndPoint(currencyUrl)
    return data

def getCurrencyExchangeRate(countryCurrencyCode, baseCode="EUR", timeIndicator="latest"):

    data = getCurrencyExchangeRates2(countryCurrencyCode, baseCode, timeIndicator)    
    return data["rates"][countryCurrencyCode]

def passAlong(countryCurrencyCode, baseCode, timeIndicator="latest"):
    data = getCurrencyExchangeRates2(countryCurrencyCode, baseCode, timeIndicator)
    return data

def convertCurrency(
    fromValue, fromCurrencyCode, toCurrencyCode, historicalDate="latest"
):
    exchangeRate = getCurrencyExchangeRate(
        toCurrencyCode, fromCurrencyCode, historicalDate
    )

    return fromValue * exchangeRate
