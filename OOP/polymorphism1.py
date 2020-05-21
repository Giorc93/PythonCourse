class Car():
    def moving(self):
        print('Moving on 4 wheels')


class Bike():
    def moving(self):
        print('Moving on 2 wheels')


class Truck():
    def moving(self):
        print('Moving on 6 wheels')


# myVehicle = Bike()

# myVehicle.moving()

# myVehicle2 = Car()

# myVehicle2.moving()

# myVehicle3 = Truck()

# myVehicle3.moving()

def vehicleMoving(vehicle):  # Defining the function
    vehicle.moving()


myVehicle3 = Truck()
myVehicle2 = Car()
vehicleMoving(myVehicle2)
