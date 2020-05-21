def numLoop2():
    numbers = []
    num = int(input('Insert a positive number: '))
    while num < 0:
        num = int(input('The number must be greater than 0, try again: '))
    newNum = int(input(
        'Insert another number, remember, this number has to be greater than the last inserted number: '))
    while newNum > num:
        numbers.append(num)
        num = newNum
        newNum = int(input(
            'Insert another number, remember, this number has to be greater than the last inserted number: '))
    print('You\'ve inserted a smaller number. End of the program')
    print(numbers)


numLoop2()

# Else on FOR or While. Executes the code after the loop has been completed
