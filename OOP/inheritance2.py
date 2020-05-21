class Vehicles():
    def __init__(self, brand, model):

        self.brand = brand
        self.model = model
        self.running = False
        self.speedUp = False
        self.brake = False

    def startEng(self):

        self.running = True

    def spdUp(self):

        self.speedUp = True

    def stop(self):

        self.brake = True

    def vehStatus(self):

        print('Brand: ', self.brand, '\nModel: ', self.model, '\nRunning: ',
              self.running, '\nSpeeding Up: ', self.speedUp, '\nBraking: ', self.brake)


class Truck(Vehicles):

    def loadStat(self, load):
        self.loaded = load
        if self.loaded == True:
            return 'Truck is loaded'
        else:
            return 'Truck is not loaded'


class electricVeh(Vehicles):

    # Object must accept the same amount of parameters as its superclass, also it must have his own parameters (if needed)
    # brand and model are the superclass parameters and authonomy is his own parameter
    def __init__(self, autho, brand, model):

        # Object inherits the superclass parameters through the super() command
        super().__init__(brand, model)
        self.authonomy = autho

    def loadBatt(self):
        # the loading prop. is given on the method, so it's not necessary on the __init__ parameters
        self.loading = True


class Motorcycle(Vehicles):
    doWheelie = ""

    def wheelie(self):
        self.doWheelie = "Doing a wheelie"

    def vehStatus(self):

        print('Brand: ', self.brand, '\nModel: ', self.model, '\nRunning: ',
              self.running, '\nSpeeding Up: ', self.speedUp, '\nBraking: ', self.brake, '\nWheelie: ', self.doWheelie)


myMotorcycle = Motorcycle('Suzuki', 'Gixxer')

myMotorcycle.wheelie()
myMotorcycle.vehStatus()

myTruck = Truck('Kenworth', 'T800')

myTruck.startEng()
myTruck.vehStatus()
print(myTruck.loadStat(True))


class electBike(electricVeh, Vehicles):

    pass


myBike = electBike(100, 'Trek', 'Marlin7 Elect')

myBike.vehStatus()
print('Authonomy: ', myBike.authonomy)

# isinstance returns true or false if the instance belongs or not to a given class
print(isinstance(myBike, electricVeh))
