class Car():

    def __init__(self):  # Same as __construct

        self.__width = 120
        self.__wheels = 4  # Encapsulation to protect the initial value
        self.__height = 80
        self.__running = False

    def startEng(self, start):

        self.__running = start

        if self.__running:
            print('Checking car status...')
            check = self.__checkCar()

        if(self.__running and check):
            return 'Car status OK. The engine is running'
        elif self.__running and check == False:
            return 'Something\'s failing, please check your car and try again.'
        else:
            return 'The engine is stopped'

    def carStatus(self):

        print('The car has: ', self.__wheels,
              ' wheels. And its width is: ', self.__width, ' cm')

    def __checkCar(self):  # Method encapsulation
        self.gas = 'Ok'
        self.oil = 'Ok'
        self.brakes = 'Ok'

        if self.gas == 'Ok' and self.oil == 'Ok' and self.brakes == 'Ok':
            return True
        else:
            return False


myCar = Car()  # Instantiating the object

print(myCar.startEng(True))
myCar.carStatus()


print('------------------Second Object----------------')
# Creating another object

myCar2 = Car()

print(myCar2.startEng(False))
myCar2.carStatus()
