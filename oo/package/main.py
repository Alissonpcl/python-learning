from models.vehicle_factory import get_vehicle_by_type, VehicleType

vehicle = get_vehicle_by_type(VehicleType.Car)

print(vehicle.get_model())
