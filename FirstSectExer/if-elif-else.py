# Use input to set two numbers, crate a function that returns the highest number

def highestNum():
    numOne = input('Insert first number: ')
    numTwo = input('Insert second number: ')
    if numOne > numTwo:
        message = "The highest number is " + numOne
    elif numTwo > numOne:
        message = "The highest number is " + numTwo
    else:
        message = "The numbers are equal"

    print(message)


highestNum()
