from tkinter import *

root = Tk()  # Creating the root, the base
root.title('First Window')  # Adding tittle
# First argument width, second height. Resizable only gets true or false.
root.resizable(1, 1)
# Adding full path to avoid error
root.iconbitmap(r'c:/wamp64/www/Python-Course/GUI/1651954-200.ico')
# Resizing window, root always resizes adjusting itself to the size of its content. Must establish frame size
root.geometry('650x350')
root.config(bg='gray')

# Creating Frame

myFrame = Frame()  # Frame created
# Packing the frame. Check Docs to see frame() options
# myFrame.pack(side='right', anchor='n') #Position of the frame
# myFrame.pack(fill='y', expand='True')  # Resizing frame on Y coord.
myFrame.pack(fill='x')  # Resizing frame on X coord.
myFrame.config(bd=8)  # Border width
myFrame.config(relief='sunken')  # Border style
myFrame.config(cursor='pirate')  # Cursor style
myFrame.config(bg='white')  # Frame color, background color
myFrame.config(width="650", height="350")  # Frame size
# Config can be applied to root

root.mainloop()  # Infinite loop the catch all the actions (events)

