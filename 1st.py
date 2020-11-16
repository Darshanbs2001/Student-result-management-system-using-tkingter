#to begin the development first we include or import the tkinter files
import tkinter as Tk
#root word or the place to store instance of the class tkinter 

win=Tk.Tk()
#since the win is a class now and the members of the class are accessed by 
#using the "."(dot operater)
#title is the member or the function that is used to name the title of your app
win.title("Python GUI")

#this is the statement that says wheter the app is able to resizeable or not and it 
#has two parameters one for the vertical(x)and one for the horizontal(y).

win.resizable(0,0)
#this is the statement that says i am still open and the app will be running until this line beyond it the app is destroyed
win.mainloop()
