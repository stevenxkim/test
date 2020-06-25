from tkinter import *
from tkinter import ttk
 

savings_balance = 0
 

def update_balance():
    global savings_balance
    deposit_amount = amount.get()
    savings_balance += deposit_amount
    total_balance = savings_balance
    account_details.set("Savings: ${:.2f}\nTotal Balance: ${:.2f}".format(savings_balance, total_balance))
    amount.set("")
 
root = Tk()
root.title("Goal Tracker")
 

message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money and see your progress towards your goals.")
 

message_label = ttk.Label(root, textvariable=message_text, wraplength=250)
message_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
 

neutral_image = PhotoImage(file="logo.png")
image_label = ttk.Label(root, image=neutral_image)
image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

account_details = StringVar()
account_details.set("Savings: $0 \nTotal balance: $0")

details_label = ttk.Label(root, textvariable=account_details)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


account_label = ttk.Label(root, text="Account: ")
account_label.grid(row=3, column=0, padx=10, pady=3)


account_names = {"Savings", "Phone", "Holiday"}
chosen_account = StringVar()
chosen_account.set(account_names[0])

account_

                              
