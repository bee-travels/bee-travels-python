from flask import Flask
from flask_restplus import Api, Resource
from services.serviceHandler import convertCurrency

app = Flask(__name__)
api = Api(
    app,
    version="1.0.0",
    title="Bee Travel Currency Data Service",
    description="This is a microservice that handles currency exchange rate data for Bee Travels",
)

currencyNS = api.namespace("currency", description="currency exchange operations")

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


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=7878)
