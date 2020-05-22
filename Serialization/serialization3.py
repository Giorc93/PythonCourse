import pickle

# Retriving the object from the binary file

retBinary = open('MyCars', 'rb')  # Opening the file on reading binary mode

# Saving the objects on the retCarList variable
retCarList = pickle.load(retBinary)

retBinary.close()  # Closing the file

for c in retCarList:
    print(c.vehStatus())  # Printing objects from the list, one by one

# Can't load the objects attributes
