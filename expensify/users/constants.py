"""
users.constants
---------------
Constants for the users app
"""

from enum import Enum


class UserTypes(Enum):
    """
    Enum class for status for the course log
    """

    FREE = 'free'
    PREMIUM = 'premium'
    ADMIN = 'admin'

    @classmethod
    def get_values(cls) -> list:
        """
        Return a list with the values of the key from the enumerator
        """
        return [key.value for key in cls]

    @classmethod
    def choices(cls):
        """
        Return the choices representation for the model
        """
        return [(key.value, key.name) for key in cls]
