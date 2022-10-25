from textwrap import indent
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np

# gui window
root = Tk()
root.title("Financulator")
root.geometry("800x800")
tabControl = ttk.Notebook(root)

# initiate multiple tabs
dashboard_tab = ttk.Frame(tabControl)
income_tab = ttk.Frame(tabControl)
expenses_tab = ttk.Frame(tabControl)
tabControl.add(dashboard_tab, text ='Dashboard')
tabControl.add(income_tab, text ='Income')
tabControl.add(expenses_tab, text ='Expenses')
tabControl.pack(expand = 1, fill ="both")

# import data from excel
df = pd.ExcelFile('database.xlsx')
month_index = df.sheet_names

sheet_list = []
for i in range(3):
  df = pd.read_excel('database.xlsx', sheet_name=month_index[i])
  sheet_list.append(df)

# remove null values 
def data_filter(data_list):
  for i in data_list:
    if pd.isnull(i):
      data_list.remove(i)
  return data_list 

# convert df into lists
income, expenses, report, asset, liability, networth = [], [], [], [], [], []
for i in range(len(sheet_list)):
    income.append([data_filter(sheet_list[i]['Income'].tolist()), data_filter(sheet_list[i]['RM'].tolist())])
    expenses.append([data_filter(sheet_list[i]['Expenses'].tolist()), data_filter(sheet_list[i]['RM.1'].tolist())])
    report.append([data_filter(sheet_list[i]['Monthly report'].tolist()), data_filter(sheet_list[i]['RM.2'].tolist())])
    asset.append([data_filter(sheet_list[i]['Asset'].tolist()), data_filter(sheet_list[i]['RM.3'].tolist())])
    liability.append([data_filter(sheet_list[i]['Liability'].tolist()), data_filter(sheet_list[i]['RM.4'].tolist())])
    networth.append(data_filter(sheet_list[i]['Networth'].tolist()))

print(income)
print(expenses)
print(report)
print(asset)
print(liability)
print(networth)

# Monthly report tab
ttk.Label(dashboard_tab, text="Monthly report").place(x = 400, y = 10)
y_pos = 10
for i in range(len(report)):
  ttk.Label(dashboard_tab, text=report[i] + "\t" + str(report_val[i])).place(x = 40, y = y_pos)
  y_pos += 50

  # Networth
ttk.Label(dashboard_tab, text="Net Worth").place(x = 400 - len("Net Worth"), y = 400)
ttk.Label(dashboard_tab, text="Asset").place(x = 200, y = 450)
ttk.Label(dashboard_tab, text="Liablity").place(x = 600, y = 450)

# Asset 
y_pos = 500
for i in range(len(asset)):
  ttk.Label(dashboard_tab, text=str(asset[i]) + "\t" + str(asset_val[i])).place(x = 200, y = y_pos)
  y_pos += 50

# Liability
y_pos = 500
for i in range(len(liability)):
  ttk.Label(dashboard_tab, text=str(liability[i]) + "\t" + str(liability_val[i])).place(x = 600, y = y_pos)
  y_pos += 50

# Income tab
ttk.Label(income_tab, text="Income sources").place(x = 400, y = 10)
y_pos = 10
for i in range(len(income)):
  ttk.Label(income_tab, text=str(income[i]) + "\t" + str(income_val[i])).place(x = 40, y = y_pos)
  y_pos += 50

# Expense tab
ttk.Label(expenses_tab, text="Expenses").place(x = 400, y = 10)
y_pos = 10
for i in range(len(expenses)):
  ttk.Label(expenses_tab, text=str(expenses[i]) + "\t" + str(expenses_val[i])).place(x = 40, y = y_pos)
  y_pos += 50

# pie custom label
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

# dashbaord figure
db_fig = Figure(figsize=(3,3), dpi=100)
report_ax = db_fig.add_subplot(111)
report_ax.bar(range(len(report)), report_val, align='edge', width=1.0)
report_bar = FigureCanvasTkAgg(db_fig, dashboard_tab)
report_bar.get_tk_widget().pack()

# dashboard net worth line graph
month = ["Jan", "Feb", "Mar"]
networth_dummydata = [8000,10000,15000]
line_fig = Figure(figsize=(3,3), dpi=100)
line_ax = line_fig.add_subplot(111)
line_ax.plot(month,networth_dummydata)
# line_ax.title('Net Worth')
# line_ax.xlabel('Month')
# line_ax.plt.ylabel('RM')
db_line = FigureCanvasTkAgg(line_fig, dashboard_tab)
db_line.get_tk_widget().pack()

# income figure
income_fig = Figure(figsize=(3, 3), dpi=100)
income_ax = income_fig.add_subplot(111)
income_ax.pie(income_val, radius=1, labels=income, labeldistance=True, autopct=make_autopct(income_val))
# ax.legend(bbox_to_anchor=(0.5, 0.5), loc='lower left')
income_pie = FigureCanvasTkAgg(income_fig, income_tab)
income_pie.get_tk_widget().pack()

# expenses figure
expenses_fig = Figure(figsize=(3,3), dpi=100)
expenses_ax = expenses_fig.add_subplot(111)
expenses_ax.pie(expenses_val, radius=1, labels=expenses, labeldistance=True, autopct=make_autopct(expenses_val))
# ax.legend(bbox_to_anchor=(0.5, 0.5), loc='lower left')
expenses_pie = FigureCanvasTkAgg(expenses_fig, expenses_tab)
expenses_pie.get_tk_widget().pack()

# canvas = Canvas()
# canvas.create_line(15, 25, 200, 25)
# canvas.pack()

if __name__ == "__main__":
  root.mainloop()