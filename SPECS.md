# General 
IBAN contains max 34 alpha-num chars containing:
    
    - country code (using ISO 3166-1 alpha-2 – two letters)
    - two check digits (checksum of the account number)
    - BBAN number that includes
        - domestic account number
        - branch identifier
        - potential routing information

Some additional rules regarding IBANs are:   

    - Permitted IBAN characters are the digits 0 to 9 and the 26 Latin alphabetic characters A to Z.  
    - In order to facilitate reading by humans, IBANs are traditionally expressed in groups of four characters separated by spaces  
    - The Basic Bank Account Number (BBAN) format is decided by the national central bank or designated payment authority of each country  
    - The check digits enable the sending bank (or its customer) to perform a sanity check of the routing destination and account number from a single string of data at the time of data entry.  

# IBAN checksum calculation

Checksum digits are the first two digits after the country code  

Checksum calculation is done using the following algorithm:
    
    1. Check that the total IBAN length is correct as per the country. If not, the IBAN is invalid.
    2. Replace the two check digits by 00 (e.g., GB00 for the UK).
    3. Move the four initial characters to the end of the string.
    4. Replace the letters in the string with digits, expanding the string as necessary, such that A or a = 10, B or b = 11, and Z or z = 35. Each alphabetic character is therefore replaced by 2 digits
    5. Convert the string to an integer (i.e. ignore leading zeroes).
    6. Calculate mod-97 of the new number, which results in the remainder.
    7. Subtract the remainder from 98 and use the result for the two check digits. If the result is a single-digit number, pad it with a leading 0 to make a two-digit number.

# Montenegro Requirements

    - Country code is `ME`  
    - IBAN length is 22  
    - BBAN length is 18  
    - Account number checksum is in the last two digits
    - Example IBAN `ME25 5050 0001 2345 6789 51`
