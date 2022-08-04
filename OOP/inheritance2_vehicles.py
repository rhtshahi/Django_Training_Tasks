# Classwork: Do for Vehicle with parameters brand, model and num of wheels. 
# Inherit it to Car and Bike, override the num of wheels attribute for car and bike respectively. 

class Vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

    def get_vehicle_info(self):
        print('')
        print('Vehicle Details:')
        print(f'Brand: {self.brand}, Model: {self.model}')
        return (self.brand, self.model)

class Car(Vehicle):
    def __init__(self, brand, model, num_of_wheels=4):
        super(Car, self).__init__(brand, model)
        self.num_of_wheels=num_of_wheels
    
    def get_car_info(self):
        print('')
        print('Car Details:')
        print(f'Brand: {self.brand}, Model: {self.model}, Number of Wheels: {self.num_of_wheels}')
        return (self.brand, self.model, self.num_of_wheels)

class Bike(Vehicle):
    def __init__(self, brand, model, wheels=2):
        super(Bike, self).__init__(brand, model)
        self.wheels=wheels

    def get_bike_info(self):
        print('')
        print('Bike Details:')
        print(f'Brand: {self.brand}, Model: {self.model}, Number of Wheels: {self.wheels}')
        return (self.brand, self.model, self.wheels)

vehicle1=Vehicle('Tata', 'Tata-1')
vehicle1.get_vehicle_info()
print(f'This is {vehicle1.brand} car of model {vehicle1.model}.')

car1=Car('Audi', 'A1')
car1.get_car_info()
print(f'This is {car1.brand} car of model {car1.model} with {car1.num_of_wheels} wheels.')

bike1=Bike('Honda', "H-1")
bike1.get_bike_info()
print(f'This is {bike1.brand} bike of model {bike1.model} with {bike1.wheels} wheels.')