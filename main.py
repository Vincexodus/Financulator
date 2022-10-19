# Calculator with basic financial konwledge

# Simple GUI with several tabs
# 1. Monthly Expenses
# - ask abt monthly gross salary
# - ask abt expenses categories 
# - rent, loan, eat, additional 

# 2. Expenses ratio 
# - 50/30/20
# - adjust accordingly

# 3. Cashflow calculator 
# - upper sheet - income & expenses
# - lower sheet - asset & liabalities

# 4. Savings calculator
# - ask amount of saving
# - user enter divided/web scrape
# - enter period of time
# - calculate total return after time

# excel or text file to store numeric data
# Rent, 400
# Loan, 400

# Excel database
# dataframe


# 1. Income
# - monthly income
# - give the option to users to add more
# - visualise data using pie chart

# 2. expenses

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Financulator")
root.geometry("800x800")
tabControl = ttk.Notebook(root)

# initiate tabs
dashboard = ttk.Frame(tabControl)
income = ttk.Frame(tabControl)
expenses = ttk.Frame(tabControl)
  
tabControl.add(dashboard, text ='Dashboard')
tabControl.add(income, text ='Income')
tabControl.add(expenses, text ='Expenses')
tabControl.pack(expand = 1, fill ="both")

income, expenses, savings, cashflow = 1000, 200, 200, 600

ttk.Label(dashboard, text="Monthly Report ").place(x = 400, y = 10)
ttk.Label(dashboard, text="Income " + str(income)).place(x = 40, y = 50)
ttk.Label(dashboard, text="Expenses " + str(expenses)).place(x = 40, y = 100)
ttk.Label(dashboard, text="Savings " + str(savings)).place(x = 40, y = 150)
ttk.Label(dashboard, text="Cash flow " + str(cashflow)).place(x = 40, y = 200)

# ttk.Button(tab1, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()