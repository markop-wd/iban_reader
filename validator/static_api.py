import json


def get_countries():
    with open("static/countries.json") as countries_fp:
        countries = json.load(countries_fp)
    return countries


def get_banks(country: str):
    with open("static/bank_codes.json") as banks_fp:
        banks = json.load(banks_fp)
    country_banks = banks.get(country, None)
    return country_banks
