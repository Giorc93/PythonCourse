# Obj: Data persistance

# Opt1: External files
# Opt2: DB

# Procedure:
# Create the external file.
# Open the file
# Manipulate the file
# Close the file

from io import open

# First parameter file name, second parameter mode to open (read, write)
textFile = open('file.txt', 'w')

line = 'Great day to code Python \nIsn\'t it?'
textFile.write(line)  # writing on the file
textFile.close()  # closing the file

textFile = open('file.txt', 'r')  # Opens the file on read mode

text = textFile.read()  # reads the file

textFile.close()  # closing the file

print(text)

textFile = open('file.txt', 'r')  # Opens the file on read mode

# reads the file line by line saving each one of themn on a list
textLines = textFile.readlines()

textFile.close()  # closes the file

print(textLines[0])

# a parameter allows to append lines to the text file
textFile = open('file.txt', 'a')

textFile.write('\nEveryday it\'s a god day to code')

textFile.close()

textFile = open('file.txt', 'r')

print(textFile.read())
print(textFile.read())  # After executing the first read command, the pointer stays at the end of the file, so the second time it's executed there are no more lines ahead and it won't print anything
# seek sets the pointer to the given position, in this case index = 0
textFile.seek(0)
print(textFile.read())
print(textFile.read(11))  # Starts reading on the given position (11)
textFile.close()

# Writing and reading mode, sets the pointer on the first postion
textFile = open('file.txt', 'r+')
