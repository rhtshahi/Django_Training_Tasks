class Vehicle:
    def __init__(self, color, brand, vehicle_type, price, no_of_wheels=4):
        self.color=color
        self.brand=brand
        self.vehicle_type=vehicle_type
        self.no_of_wheels=no_of_wheels
        self.price=price

    def get(self):
        print('')
        print(f'Vehicle Description: Brand: {self.brand}, Vehicle Type: {self.vehicle_type}, Price: Rs.{self.price}, Wheels:{self.no_of_wheels}')

Car=Vehicle('Black', 'Audi', 'Car', '50,00,000', 4)
Truck=Vehicle('Green', 'Tata', 'Truck', '30,00,000', 6)
Bike=Vehicle('Red', 'Honda', 'Bike','10,00,000',2)

print(Vehicle.get(Car))
print(Vehicle.get(Truck))
print(Vehicle.get(Bike))