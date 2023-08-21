import json
from pathlib import Path


def store_iban(iban: str, validity: bool, time: str):
    store_iban_json(iban, validity, time)


def store_iban_json(iban, validity, time):
    if not Path("storage.json").exists():
        storage_json = open("storage.json", "w")
        storage_json.write("[]")
        storage_json.close()

    with open("storage.json", "r") as storage_fp:
        # TODO - Check if it's an empty file or a list
        storage_json = json.load(storage_fp)
    storage_json.append({"iban": iban, "validity": validity, "time": time})

    with open("storage.json", "w") as storage_fp:
        json.dump(storage_json, storage_fp, indent=4)


def store_iban_csv(iban, validity, time):
    pass


def display_ibans():
    storage_json = _return_ibans()
    for iban_attempt in storage_json:
        print(f"Valid: '{iban_attempt['validity']}', Time: '{iban_attempt['time']}', IBAN: '{iban_attempt['iban']}'" )
    return


def _return_ibans():
    with open("storage.json", "r") as storage_fp:
        storage_json = json.load(storage_fp)
    return storage_json
