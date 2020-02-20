from flask import Flask
from flask_restplus import Api, Resource, fields
from services.serviceHandler import convert_currency, get_currency_exchange_rates
from services.countryCurrencyCodeHandler import (
    get_country_and_currency_code,
    get_currency_name_and_code,
)

app = Flask(__name__)
api = Api(
    app,
    version="1.0.0",
    title="Bee Travels Currency Data Service",
    description="This is a microservice that handles currency exchange rate data for Bee Travels",
)

currencyNS = api.namespace(
    "Currency",
    description="Operations associated with currency exchange rate conversions",
)


currencyCodeCountryModel = api.model(
    "currencyCodeCountryModel",
    {
        "currencyCode": fields.String(
            required=False, description="3 letter currency code"
        ),
        "country": fields.String(required=False, description="country name"),
    },
)


@currencyNS.route("/")
class CurrencyList(Resource):
    """Shows a list of currency ex rates"""

    def get(self):
        return get_currency_exchange_rates()


@currencyNS.route("/<int:currencyFromAmount>/<currencyFromCode>/<currencyToCode>")
@currencyNS.response(404, "Currency Code not found")
@currencyNS.param("currencyFromAmount", "currency to convert from value (float)")
@currencyNS.param("currencyFromCode", "currency (3 character code) to convert from")
@currencyNS.param("currencyToCode", "currency (3 character code) to convert to")
class Currency(Resource):
    def get(self, currencyFromAmount, currencyFromCode, currencyToCode):

        result = convert_currency(
            float(currencyFromAmount), currencyFromCode, currencyToCode
        )
        return {"result": result}


@currencyNS.route("/search")
@currencyNS.response(404, "Currency Code not found")
class Search(Resource):
    @currencyNS.doc("search_currency_meta")
    @currencyNS.expect(currencyCodeCountryModel)
    @currencyNS.marshal_with(currencyCodeCountryModel, code=201)
    def post(self):
        if "currencyCode" in api.payload:
            return get_country_and_currency_code(api.payload["currencyCode"])
        elif "country" in api.payload:
            return get_currency_name_and_code(api.payload["country"])
        else:
            api.abort(400, "Pass in either the currencyCode or country name")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=7878)
