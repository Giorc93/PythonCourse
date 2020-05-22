# Encoding an object on binary to make easier its distribution
# Pickle library its needed

import pickle  # Contains the needed methods to serialize the file

namesList = ['Gio', 'Andres', 'Liz', 'Natalia']

# Creating the binary file, the second argument especifies the binary writing mode
binaryFile = open('NameList', 'wb')

# Dumping the list on the binary file

pickle.dump(namesList, binaryFile)

binaryFile.close()

del (binaryFile)  # Deleting binaryFile from the memory

# Restoring the binary file

file = open('NameList', 'rb')  # Reading binary mode

listFile = pickle.load(file)  # Loading the binary file

print(listFile)  # Printing the data inside the loaded file
