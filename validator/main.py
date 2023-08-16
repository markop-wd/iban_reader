import argparse
from argparse import ArgumentParser
from static_api import get_countries
from storage import store_iban, display_ibans
import logging

from validators import Validators

logger = logging.getLogger(__name__)


def validate_ibans(file_path: str):
    with open(file_path, "r") as ibans_fp:
        input_ibans = ibans_fp.readlines()
    for iban in input_ibans:
        validate_iban(iban)


def validate_iban(iban: str) -> bool:
    store_iban(iban)
    iban = iban.replace(" ", "").upper()
    country = get_country(iban)
    country_validator = Validators.get_validator(country)
    if not country_validator:
        logger.error("Validator for that country is not implemented.")
    validator = country_validator(iban)
    if not validator.validate():
        logger.error(f"Invalid IBAN: {iban} for country: {country}")
        return False
    return True


def get_country(iban):
    countries = get_countries()
    country = iban[:2]
    if country not in countries:
        logger.error("Country code is not valid.")
        return False
    else:
        return iban[:2]


def parse_cli():
    arg_parser = ArgumentParser(
        description="IBAN Validator",
        prog="IBAN Validator",
        usage="\nProvide either a singular IBANs or a file with multiple IBANs to validate\n"
        "Alternatively display the previously checked IBANs",
    )
    arg_parser.add_argument("-i", "--iban", type=str, help="Which IBAN to validate")
    arg_parser.add_argument("-f", "--file", type=str, help="File with a list of IBANs")
    arg_parser.add_argument(
        "-d",
        "--display_previous",
        action="store_true",
        help="Display previously inputted IBANs",
    )
    arg_parser.add_argument(
        "-v",
        "--verbosity",
        help="Set the verbosity level of the logger. Accepts either the "
        "textual/string options [ERROR, WARNING, INFO,"
        "DEBUG] or their integer counterparts [0,1,2,3]",
        default="1",
        type=log_level_parser,
    )

    args = arg_parser.parse_args()
    return args


def setup_logger(verbosity):
    if verbosity.upper() == "DEBUG":
        log_format = (
            "%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
        )
    else:
        log_format = "%(asctime)s - %(levelname)s - %(message)s"

    logging.basicConfig(
        level=verbosity.upper(),
        format=log_format,
    )


def log_level_parser(log_level: str) -> str:
    all_log_levels = {0: "ERROR", 1: "WARNING", 2: "INFO", 3: "DEBUG"}

    try:
        level = int(log_level)
        if level in all_log_levels:
            return all_log_levels[level].upper()
        else:
            raise argparse.ArgumentTypeError(f"Invalid log level: {log_level}")
    except ValueError:
        log_level_upper = log_level.upper()
        if log_level_upper in all_log_levels.values():
            return log_level_upper
        else:
            raise argparse.ArgumentTypeError(f"Invalid log level: {log_level}")


def main():
    args = parse_cli()
    setup_logger(args.verbosity)
    if args.display_previous:
        display_ibans()
    elif args.iban:
        validate_iban(args.iban)
    elif args.file:
        validate_ibans(args.file)
    else:
        logger.error("Please choose an input, use -h to see the usage")


if __name__ == "__main__":
    main()
