def add(a, b):
    return a + b


def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Can\'t divide by 0')
        return 'Try again with another number'

# Except only works if the error passed on the except line is the same error that's causing the program to fail
