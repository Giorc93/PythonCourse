# Insert name, addres and phone, save the data on a list and print the data

def showData():
    name = input('What\'s your name? ')
    address = input('Where do you live?G ')
    phone = input('What\'s your phone number? ')

    data = [name, address, phone]

    print('Is your data ok? : Name: '+data[0] +
          ' Address: '+data[1]+' Phone Number: '+data[2])


showData()
