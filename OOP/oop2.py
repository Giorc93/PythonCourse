class Car():

    def __init__(self):  # Same as __construct

        self.__width = 120
        self.__wheels = 4  # Encapsulation to protect the initial value
        self.__height = 80
        self.__running = False

    def startEng(self, start):

        self.__running = start

        if(self.__running):
            return 'The engine is running'
        else:
            return 'The engine is stopped'

    def carStatus(self):

        print('The car has: ', self.__wheels,
              ' wheels. And its width is: ', self.__width, ' cm')


myCar = Car()  # Instantiating the object

print(myCar.startEng(True))
myCar.carStatus()

# Creating another object

myCar2 = Car()

print(myCar2.startEng(False))
myCar2.__wheels = 2
myCar2.carStatus()
