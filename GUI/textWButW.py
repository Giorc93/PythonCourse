from tkinter import *

root = Tk()
root.title('Datos')

myFrame = Frame(root, width=450, height=650)
myFrame.pack()

myName = StringVar()  # Creating the variable type string

# textvariable assigning the variable myName to the entry widget
nameFrame = Entry(myFrame, textvariable=myName)
nameFrame.grid(row=0, column=1, padx=4, pady=4)
nameFrame.config(fg='green', justify='center')

nameLabel = Label(myFrame, text='Nombre: ')
nameLabel.grid(row=0, column=0, sticky='e')


lastnaFrame = Entry(myFrame)
lastnaFrame.grid(row=1, column=1, padx=4, pady=4)
lastnaFrame.config(fg='green', justify='center')

lastnaLabel = Label(myFrame, text='Apellido: ')
lastnaLabel.grid(row=1, column=0, sticky='e')


ageFrame = Entry(myFrame)
ageFrame.grid(row=2, column=1, padx=4, pady=4)
ageFrame.config(fg='green', justify='center')

ageLabel = Label(myFrame, text='Edad: ')
ageLabel.grid(row=2, column=0, sticky='e')


passFrame = Entry(myFrame)
passFrame.grid(row=3, column=1, padx=4, pady=4)
passFrame.config(fg='red', justify='center', show='*')

passLabel = Label(myFrame, text='Contraseña: ')
passLabel.grid(row=3, column=0, sticky='e')


commFrame = Text(myFrame, width=15, height=8)  # Text widget
commFrame.grid(row=4, column=1, padx=4, pady=4)
vertScroll = Scrollbar(myFrame, command=commFrame.yview)
# Placing the scrollbar to the right side of the comment widget
# sticky='nsew' allows the scrollbar to adjust its size according to the size of the widget, in this case the textwidget
vertScroll.grid(row=4, column=2, sticky='nsew')
# yscrollcommand allows the scrollbar to place the scroll bar depending on which line you're placed
commFrame.config(fg='green', yscrollcommand=vertScroll.set)

commLabel = Label(myFrame, text='Contraseña: ')
commLabel.grid(row=4, column=0, sticky='e')


def buttonCode():
    # Creating a function to set the variable value after the button is pressed
    myName.set('Gio')


# command executes the defined function after clicking the button
sendButton = Button(root, text='Enviar', command=buttonCode)
sendButton.pack()


root.mainloop()
