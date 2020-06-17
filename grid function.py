from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Grid Test")

button1 = ttk.Button(root,text="Row 0, Col 0")
button1.grid(row=0,column=0)

button2 = ttk.Button(root, text="Row 1, Col 2")
button2.grid(row=1, column=2)
 
button3 = ttk.Button(root, text="Row 2, Col 2")
button3.grid(row=2, column=2)
 
button4 = ttk.Button(root, text="Row 1, Col 0")
button4.grid(row=1, column=0)
 
button5 = ttk.Button(root, text="Row 0, Col 1")
button5.grid(row=0, column=1)
 
button6 = ttk.Button(root, text="Row 0, Col 2")
button6.grid(row=0, column=2)
 
button7 = ttk.Button(root, text="Row 1, Col 1")
button7.grid(row=1, column=1)
 
button8 = ttk.Button(root, text="Row 2, Col 1")
button8.grid(row=2, column=1)
 
button9 = ttk.Button(root, text="Row 2, Col 0")
button9.grid(row=2, column=0)
root.mainloop()


from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Grid Test")

button1 = ttk.Button(root, text="Row 0, Col 0")
button1.grid(row=0, column=0)

button2 = ttk.Button(root, text="Row 0, Col 1")
button2.grid(row=0, column=1)

button3 = ttk.Button(root, text="Row 0, Col 2")
button3.grid(row=0, column=2)

button4 = ttk.Button(root, text="Row 1, Col0")
button4.grid(row=1, column=0, columnspan=3, sticky="WE")

button5 =ttk.Button(root, text="Row 1, Col 0)"




