# Serializing an object and retrieving its data
import pickle


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


myCar1 = Vehicles('Ferrari', 'Spider')
myCar2 = Vehicles('Porsche', '911')
myCar3 = Vehicles('Audi', 'Q3')

myCars = [myCar1, myCar2, myCar3]

objBinaryFile = open('MyCars', 'wb')  # Creating the binary file

pickle.dump(myCars, objBinaryFile)  # Dumping the object into the binary file

objBinaryFile.close()

del (objBinaryFile)

# Retriving the object from the binary file

retBinary = open('MyCars', 'rb')  # Opening the file on reading binary mode

# Saving the objects on the retCarList variable
retCarList = pickle.load(retBinary)

retBinary.close()  # Closing the file

for c in retCarList:
    print(c.vehStatus())  # Printing objects from the list, one by one
