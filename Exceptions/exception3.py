import math


def sqrtFunc(a):

    if a < 0:
        raise ValueError('Number should be grater than 0')
    else:
        return math.sqrt(a)


op1 = (int(input('Insert a number: ')))
try:
    print(sqrtFunc(op1))
except ValueError as NegativeNumber:
    print(NegativeNumber)

print('Program ended')
