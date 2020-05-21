def checkAge(age):
    if age < 0:
        # Creating the exception
        raise TypeError('The age is not valid. Should be greater than 0')
    if age < 20:
        return "Too young"
    if age < 40:
        return 'Young'
    if age < 65:
        return 'Mature'
    if age < 100:
        'Take care of yourself'


print(checkAge(-9))

# After showing the error the program will stop. Should use the try and catch block to keep the program runing
