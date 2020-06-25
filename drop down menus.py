from tkinter import *

 from tkinter import ttk


root = Tk()
 root.title("My GUI App")

Label1 = ttk.Label(root,text="My GUI App!")
 label1.grid(row=0,column=0,padx=10,pady=5)

words = stringVar()

words_entry = ttk.Entry(root,textvariable=words)
 words_entry.grid(row=1, column=0, padx=10, pady=5)

label2 = ttk.Label(root,textvariable=words,wraplength=150)
 label2.grid(row=2, column=0, padx=10, pady=5)

chosen_option = StringVar()
 
