class Vehicle :
    def type(self) :
        print("This a type of vehicle")

class Car(Vehicle) :
    def type(self):
        print("This is Sedan")

class Plane(Vehicle) :
    def type(self) : 
        print("This is a A380")

for vehicle in [Car(),Plane()] :
    vehicle.type()