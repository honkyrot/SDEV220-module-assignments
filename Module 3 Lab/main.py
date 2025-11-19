# M03 Lab - Case Study: Lists, functions, and classes
# created on 11/9/2023 by honkyrot

class Vehicle:
    """superclass representing any vehicle"""

    def __init__(self, vehicle_type: str = None) -> None:
        """innit"""
        self.vehicle_type = vehicle_type

    def get_vehicle_type(self) -> None:
        """get user to input vehicle type"""
        self.vehicle_type = input("Enter the type of vehicle: ")


class Automobile(Vehicle):
    """automobile with attribute descriptions"""

    def __init__(self, vehicle_type: str = None, year: float = None, make: str = None, model: str = None, doors: float = None, roof: str = None) -> None:
        """init"""
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def print_vehicle(self) -> None:
        """print vehicle"""
        print(f"Vehicle Type: {self.vehicle_type}\n"
              f"Year: {self.year}\n"
              f"Make: {self.make}\n"
              f"Model: {self.model}\n"
              f"Doors: {self.doors}\n"
              f"Roof: {self.roof}")

    def create_information(self) -> None:
        """get user input to create or change anything"""
        self.year = input("Enter the year of the vehicle: ")
        self.make = input("Enter the make of the vehicle: ")
        self.model = input("Enter the model of the vehicle: ")
        self.doors = input("Enter the number of doors of the vehicle: ")
        self.roof = input(
            "Enter the roof type of the vehicle (sun roof or solid): ")

input_vehicle_type = input("Enter the type of vehicle: ")
your_vehicle = Vehicle(input_vehicle_type)
input_year = input("Enter the year of the vehicle: ")
input_make = input("Enter the make of the vehicle: ")
input_model = input("Enter the model of the vehicle: ")
input_doors = input("Enter the number of doors of the vehicle: ")
input_roof = input("Enter the roof type of the vehicle (sun roof or solid): ")
your_auto = Automobile(input_vehicle_type, input_year, input_make,
                       input_model, input_doors, input_roof)
your_auto.print_vehicle()
