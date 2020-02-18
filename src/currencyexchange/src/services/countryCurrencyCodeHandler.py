import os
import csv

class NotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        
class InvalidCountryCode(Exception):
    def __init__(self, message):
        self.message = message      
        
def read_data():
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


def get_currency_name_and_code(countryName):
    data = read_data()
    for row in data:
        if row["country"].upper() == countryName.upper():
            return row
    raise NotFoundError(f"country {countryName} does not exist")


def get_country_and_currency_code(currencyCode):
    """ note pythonic way - use list comprehensions """
    data = read_data()
    if len(currencyCode.strip()) != 3:
        raise InvalidCountryCode(f"currencyCode {currencyCode} should only be 3 characters long")
    matches = [v for v in data if v["currencyCode"].upper() == currencyCode.upper()]
    
    if len(matches) == 0: 
        raise NotFoundError(f"currencyCode  {currencyCode} not found in our datafile")
    
    return {
        "currencyCode": matches[0]["currencyCode"],
        "currencyName": matches[0]["currencyName"],
        "country": [m["country"] for m in matches],
    }
