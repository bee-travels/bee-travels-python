from flask import Flask
from services.serviceHandler import convertCurrency
import logging

logger = logging.getLogger(__name__)
app = Flask(__name__)


# /currency/{currencyFromAmount}/{currencyFromCode}/{currencyToCode}
#  /currency/10/EUR/USD


@app.route("/currency/<currencyFromAmount>/<currencyFromCode>/<currencyToCode>")
def getCurrency(currencyFromAmount, currencyFromCode, currencyToCode):
    result = convertCurrency(
        float(currencyFromAmount), currencyFromCode, currencyToCode
    )
    return {"result": result}


if __name__ == "__main__":
    """ this should be in the program's main/start/run function """
    # import logging.config

    # logging.config.fileConfig("logging.conf")
    # logger = logging.getLogger(__name__)
    app.run(debug=True)
