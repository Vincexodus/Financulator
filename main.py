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
# - upper sheet - income_tab) & expenses
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

from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

# new window
root = Tk()
root.title("Financulator")
root.geometry("800x800")
tabControl = ttk.Notebook(root)

# initiate tabs
dashboard_tab = ttk.Frame(tabControl)
income_tab = ttk.Frame(tabControl)
expenses_tab = ttk.Frame(tabControl)
  
tabControl.add(dashboard_tab, text ='Dashboard')
tabControl.add(income_tab, text ='Income')
tabControl.add(expenses_tab, text ='Expenses')
tabControl.pack(expand = 1, fill ="both")

# data
df = pd.read_excel('database.xlsx')
# df = pd.DataFrame()
print(df)
income = df['Income'].tolist()
income_val = df.iloc[:, 1].tolist()
expenses = df['Expenses'].tolist()
expenses_val = df.iloc[:, 3].tolist()
report = df['Monthly report'].tolist()
report_val = df.iloc[:, 5].tolist()

y_pos = 10
# Monthly report
ttk.Label(dashboard_tab, text="Monthly report").place(x = 400, y = 10)
for i in range(len(income)):
  ttk.Label(dashboard_tab, text=report[i] + "\t" + str(report_val[i])).place(x = 40, y = y_pos)
  y_pos += 50

# Income tab
y_pos = 10
ttk.Label(income_tab, text="Income sources").place(x = 400, y = 10)
for i in range(len(income)):
  ttk.Label(income_tab, text=str(income[i]) + "\t" + str(income_val[i])).place(x = 40, y = y_pos)
  y_pos += 50

# pie custom label
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

# dashboard_tab pie
savings, cashflow = 100, 100
pie_label = ["Income", "Expenses", "Savings", "Cashflow"]
pie_val = [report_val[0], report_val[1], savings, cashflow]
fig = Figure(figsize=(3,3), dpi=100)
ax = fig.add_subplot(122)

ax.pie(pie_val, radius=1, labels=pie_label, labeldistance=None, autopct=make_autopct(pie_val))
ax.legend(bbox_to_anchor=(1, 1), loc='lower left')
pie_chart = FigureCanvasTkAgg(fig, dashboard_tab)
# pie_chart.get_tk_widget().pack(fill=BOTH, expand= True)
pie_chart.get_tk_widget().pack()

# ttk.Button(income), text="Edit", command=root.destroy).grid(column=1, row=0)
# ttk.Button(income, text="Edit", command=root.destroy).grid(column=2, row=0)
if __name__ == "__main__":
 root.mainloop() 
