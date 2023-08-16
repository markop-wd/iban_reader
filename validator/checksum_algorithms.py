def mod97_regular_checksum(iban: str) -> bool:
    """
    Function for validation of the IBAN checksum
    More on calculating the checksum is located in the requirements

    :param iban: IBAN which to check
    :return: whether the provided IBAN checksum matches the calculated value
    """
    # First replace the checksum values with 00 so instead of ME25 we have ME00
    mod_iban = iban[:2] + "00" + iban[4:]
    # Put the country code and checksum at the end of the IBAN
    mod_iban = mod_iban[4:] + mod_iban[:4]
    # Convert the alphabet characters to integer values - A=10, B=11 etc.
    iban_digits = "".join(
        str(ord(char) - 55) if char.isalpha() else char for char in mod_iban
    )
    iban_int = int(iban_digits)
    checksum = 98 - (iban_int % 97)
    # If we get 1 convert it to 01
    checksum = str(checksum).rjust(2, "0")
    if checksum == iban[2:4]:
        return True
    else:
        return False
