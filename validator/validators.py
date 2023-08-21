import logging
from abc import abstractmethod, ABC
from validator.static_api import get_banks

from validator.checksum_algorithms import mod97_regular_checksum

logger = logging.getLogger(__name__)


class Base(ABC):
    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def check_bban(self):
        pass


class Montenegro(Base):
    def __init__(self, iban):
        self.iban = iban

    def validate(self) -> bool:
        if self.iban[2:4] != "25":
            logger.error("Checksum for Montenegro must always be 25")
            return False
        if len(self.iban) != 22:
            logger.error("Length for Montenegro must always be 22")
            return False
        if not mod97_regular_checksum(self.iban):
            logger.error("Checksum algorithm didn't return 25")
            return False
        if not self.check_bban():
            logger.error("Bank code in BBAN is not valid")
            return False

        return True

    def check_bban(self):
        banks = get_banks("ME")
        bban = self.iban[4:]
        try:
            bank_code = int(bban[:3])
        except ValueError:
            return False
        if bank_code not in banks.values():
            return False
        return True


class Validators:
    validator_classes = {"ME": Montenegro}

    @classmethod
    def get_validator(cls, country: str):
        return cls.validator_classes.get(country, None)
