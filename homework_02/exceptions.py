"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __str__(self):
        return "Low Fuel!"


class NotEnoughFuel(Exception):
    def __str__(self):
        return "Not Enough Fuel!"


class CargoOverload(Exception):
    def __str__(self):
        return "Over Load!"
