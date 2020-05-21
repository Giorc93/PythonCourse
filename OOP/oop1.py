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
