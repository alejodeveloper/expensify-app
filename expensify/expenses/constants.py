"""
expenses.constants
------------------
Enum Constants for expenses app
"""
from enum import Enum


class ExpenseTypeSlug(Enum):
    """
    Enum class for status for the course log
    """

    FOOD = 'food'
    HOSE_SERVICES = 'house-services'
    TRANSPORTATION = 'transportation'
    DRINKS_PARTIES = 'drinks-parties'
    HOBBIES = 'hobbies'
    SPORTS = 'sports'
    CLOTHING = 'clothing'
    FURNITURE = 'FURNITURE'
    HOME_APPLIANCE = 'home-appliance'

    @classmethod
    def get_values(cls) -> dict:
        """
        Return a dict with the values of the key from the enumerator
        """
        return {key.value: key.value for key in cls}

    @classmethod
    def choices(cls):
        """
        Return the choices representation for the model
        """
        return [(key.value, key.name) for key in cls]


class GeneralConstants(Enum):
    DATE_STRFORMAT = "%Y-%m-%dTHH:mm:ssZ"
