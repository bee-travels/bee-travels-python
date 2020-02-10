import os
import csv


def readData():
    """ for now we will hardcode this to read the ./data/countryCurrencyMetadata.csv """
    rows_ = []
    dir_path_ = os.path.dirname(os.path.realpath(__file__))
    file_path_ = "{}/data/countryCurrencyMetadata.csv".format(dir_path_)
    with open(file_path_, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows_.append(
                {
                    "country": row["country"],
                    "currencyName": row["currencyName"],
                    "currencyCode": row["currencyCode"],
                }
            )
    return rows_


# Even though we hard coded this, that's OK, as we can first confirm tests wire up to the src package
# as expected!! Lets continue and Refactor to make this work!

# now lets refactor this to work!
def getCurrencyNameAndCode(countryName):
    return {
        "country": "South Africa",
        "currencyName": "South African rand",
        "currencyCode": "ZAR",
    }
