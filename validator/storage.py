def store_iban(iban: str):
    with open("storage.json", "a") as storage_fp:
        storage_fp.write(f"{iban}\n")


def display_ibans():
    iban_list = _return_ibans()
    print(iban_list)
    return iban_list


def _return_ibans():
    with open("storage.json", "r") as storage_fp:
        iban_list = storage_fp.read().splitlines()
    return iban_list
