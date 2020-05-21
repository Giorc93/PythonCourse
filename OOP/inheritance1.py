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


class Motorcycle(Vehicles):
    pass


myMotorcycle = Motorcycle('Suzuki', 'Gixxer')

myMotorcycle.vehStatus()
