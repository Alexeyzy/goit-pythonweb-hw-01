import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)
 
 
class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info("%s %s: Двигун запущено", self.make, self.model)


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info("%s %s: Мотор заведено", self.make, self.model)


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} (EU Spec)")


def run_factory_task() -> None:
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicles: list[Vehicle] = [
        us_factory.create_car("Ford", "Mustang"),
        us_factory.create_motorcycle("Harley-Davidson", "Sportster"),
        eu_factory.create_car("Volkswagen", "Golf"),
        eu_factory.create_motorcycle("BMW", "R 1250 GS"),
    ]

    for vehicle in vehicles:
        vehicle.start_engine()