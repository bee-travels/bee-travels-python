from flask import Flask
from flask_restplus import Api, Resource, fields
from services.serviceHandler import convertCurrency, getCurrencyExchangeRates
from services.countryCurrencyCodeHandler import (
    getCountryAndCurrencyCode,
    getCurrencyNameAndCode,
)


app = Flask(__name__)
api = Api(
    app,
    version="1.0.0",
    title="Bee Travel Currency Data Service",
    description="This is a microservice that handles currency exchange rate data for Bee Travels",
)

currencyNS = api.namespace("currency", description="currency exchange operations")


currencyObject = api.model(
    "CurrencyObject",
    {
        "currencyCode": fields.String(
            required=False, description="3 letter currency code"
        ),
        "country": fields.String(required=False, description="country name"),
    },
)


@currencyNS.route("/")
class CurrencyList(Resource):
    @currencyNS.doc("list currency exchange rates")
    def get(self):
        return getCurrencyExchangeRates()


#  /currency/{currencyFromAmount}/{currencyFromCode}/{currencyToCode}
#  /currency/10/EUR/USD


@currencyNS.route("/<int:currencyFromAmount>/<currencyFromCode>/<currencyToCode>")
@currencyNS.response(404, "Currency Code not found")
@currencyNS.param("currencyFromAmount", "currency to convert from value (float)")
@currencyNS.param("currencyFromCode", "currency (3 character code) to convert from")
@currencyNS.param("currencyToCode", "currency (3 character code) to convert to")
class Currency(Resource):
    def get(self, currencyFromAmount, currencyFromCode, currencyToCode):

        result = convertCurrency(
            float(currencyFromAmount), currencyFromCode, currencyToCode
        )
        return {"result": result}


@currencyNS.route("/search")
@currencyNS.response(404, "Currency Code not found")
class Search(Resource):
    @currencyNS.doc("search_currency_meta")
    @currencyNS.expect(currencyObject)
    @currencyNS.marshal_with(currencyObject, code=201)
    def post(self):
        if "currencyCode" in api.payload:
            return getCountryAndCurrencyCode(api.payload["currencyCode"])
        elif "country" in api.payload:
            return getCurrencyNameAndCode(api.payload["country"])
        else:
            api.abort(400, "Pass in either the currencyCode or country name")


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=7878)
