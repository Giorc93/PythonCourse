# import modules
# Importing everything using *. Keep in mind the optimization when loading everything on a module
from modules2 import *
from modules import *

# from modules import sumNm
# from modules import subtNm
# from modules import multNm

sumNm(7, 4)
subtNm(36, 3)
multNm(4, 6)

myBike = Motorcycle('Royal Enfield', 'Himalayan')

myBike.wheelie()
myBike.vehStatus()
