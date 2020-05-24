from tkinter import *

root = Tk()  # Creating the root, the base
root.title('First Window')  # Adding tittle
# First argument width, second height. Resizable only gets true or false.
root.resizable(1, 1)
# Adding full path to avoid error
root.iconbitmap(r'c:/wamp64/www/Python-Course/GUI/1651954-200.ico')
root.geometry('650x350')  # Resizing window
root.config(bg='gray')

root.mainloop()  # Infinite loop the catch all the actions (events)
