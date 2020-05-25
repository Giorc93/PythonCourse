from tkinter import *

root = Tk()  # Creating Root
root.title('Datos')

myFrame = Frame(root, width=450, height=650)  # Creating Frame
myFrame.pack()  # packing the frame

nameFrame = Entry(myFrame)  # Creating entry label
# nameFrame.place(x=100, y=150)  # Placing the entry label
nameFrame.grid(row=0, column=1, padx=4, pady=4)
nameFrame.config(fg='green', justify='center')
nameLabel = Label(myFrame, text='Nombre: ')
# nameLabel.place(x=100, y=150)  # Place is not the bes way to align labels
# Sticky allows to align the text (North, east, south, west)
nameLabel.grid(row=0, column=0, sticky='e')

lastnaFrame = Entry(myFrame)
# .grid allows to place the objects trough row and columns coordinates
lastnaFrame.grid(row=1, column=1, padx=4, pady=4)
lastnaFrame.config(fg='green', justify='center')
lastnaLabel = Label(myFrame, text='Apellido: ')
lastnaLabel.grid(row=1, column=0, sticky='e')

ageFrame = Entry(myFrame)
# Padding: padx and pady establishes the padding on the X or Y coordinate
ageFrame.grid(row=2, column=1, padx=4, pady=4)
ageFrame.config(fg='green', justify='center')
ageLabel = Label(myFrame, text='Edad: ')
ageLabel.grid(row=2, column=0, sticky='e')

passFrame = Entry(myFrame)
# Padding: padx and pady establishes the padding on the X or Y coordinate
passFrame.grid(row=3, column=1, padx=4, pady=4)
passFrame.config(fg='red', justify='center', show='*')
passLabel = Label(myFrame, text='Contraseña: ')
passLabel.grid(row=3, column=0, sticky='e')


root.mainloop()
