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

    def __init__(self, autho, brand, model):

        super().__init__(brand, model)
        self.authonomy = autho

    def loadBatt(self):

        self.loading = True


class Motorcycle(Vehicles):
    doWheelie = ""

    def wheelie(self):
        self.doWheelie = "Doing a wheelie"

    def vehStatus(self):

        print('Brand: ', self.brand, '\nModel: ', self.model, '\nRunning: ',
              self.running, '\nSpeeding Up: ', self.speedUp, '\nBraking: ', self.brake, '\nWheelie: ', self.doWheelie)
