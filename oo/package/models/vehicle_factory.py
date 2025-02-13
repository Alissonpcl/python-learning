from enum import Enum

from oo.package.models.base_vehicle import Vehicle
from oo.package.models.bike_vehicle import BikeVehicle
from oo.package.models.car_vehicle import CarVehicle


class VehicleType(Enum):
    Car = "Car",
    Bike = "Bike"


def get_vehicle_by_type(vehicle_type: VehicleType) -> Vehicle:
    if vehicle_type == VehicleType.Bike:
        return BikeVehicle()

    if vehicle_type == VehicleType.Car:
        return CarVehicle()
