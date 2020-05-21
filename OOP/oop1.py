class Car():
    width = 120
    wheels = 4
    height = 80
    running = False

    def startEng(self):
        self.running = True

    def engStat(self):
        if(self.running):
            return 'The engine is running'
        else:
            return 'The engine is stopped'


myCar = Car()  # Instantiating the object

print(myCar.height)
print(myCar.wheels)
print(myCar.running)

myCar.startEng()
print(myCar.engStat())

# Creating another object

myCar2 = Car()

print(myCar2.height)
print(myCar2.wheels)
print(myCar2.running)

print(myCar2.engStat())
