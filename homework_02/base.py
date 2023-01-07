from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    def __init__(self, weight=100, fuel=40, fuel_consumption=3, started=False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if self.fuel <= 0:
            raise LowFuelError
        else:
            self.started = True

    def move(self, distance):
        if (self.fuel_consumption * distance) > self.fuel:
            raise NotEnoughFuel
        else:
            self.fuel -= self.fuel_consumption * distance