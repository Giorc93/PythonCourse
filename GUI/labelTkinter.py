# Widget used to show text or images. Does not allow any interaction

# labelVar = Label(container, options) Check DOC for options

from tkinter import *

root = Tk()
root.title('Label Examples')

myFrame = Frame(root, width=500, height=400)
myFrame.pack()
# Tkinter only works with png and gif images
# Check size doc
myImg = PhotoImage(file='c:/wamp64/www/Python-Course/GUI/giphy.gif')

# myLabel = Label(myFrame, text='Hello World')
# myLabel.place(x=100, y=200) or
# Label(myFrame, text='Hello World', fg='red',
#       font=('Teko', 18)).place(x=100, y=200) For text labels
Label(myFrame, image=myImg).place(x=100, y=200)  # For image labels

root.mainloop()
