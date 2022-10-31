from cProfile import label
from shelve import DbfilenameShelf
from tkinter import *
from tkinter import ttk
from turtle import color
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from datetime import date
from PIL import ImageTk, Image

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

# pie custom label
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

# convert df into lists
income, expenses, report, asset, liability, networth = [], [], [], [], [], []
for i in range(len(sheet_list)):
    income.append([data_filter(sheet_list[i]['Income'].tolist()), data_filter(sheet_list[i]['RM'].tolist())])
    expenses.append([data_filter(sheet_list[i]['Expenses'].tolist()), data_filter(sheet_list[i]['RM.1'].tolist())])
    report.append([data_filter(sheet_list[i]['Monthly report'].tolist()), data_filter(sheet_list[i]['RM.2'].tolist())])
    asset.append([data_filter(sheet_list[i]['Asset'].tolist()), data_filter(sheet_list[i]['RM.3'].tolist())])
    liability.append([data_filter(sheet_list[i]['Liability'].tolist()), data_filter(sheet_list[i]['RM.4'].tolist())])
    networth.append(data_filter(sheet_list[i]['Networth'].tolist()))

# print(income)
# print(expenses)
# print(report)
# print(asset)
# print(liability)
# print(networth)

curr_month = date.today().month

for month in month_index:
  if(curr_month == int(month.split('-')[0])):
    month_income = income[month_index.index(month)]
    month_expenses = expenses[month_index.index(month)]
    month_report = report[month_index.index(month)]
    month_asset = asset[month_index.index(month)]
    month_liability = liability[month_index.index(month)]
    month_networth = networth[month_index.index(month)]

# Monthly report label 
ttk.Label(dashboard_tab, text="Monthly report", font= ('Arial', 15)).place(x = 40, y = 10)
y_pos = 60
for i in range(len(month_report[0])):
  ttk.Label(dashboard_tab, text=month_report[0][i] + "\t" + str(month_report[1][i])).place(x = 40, y = y_pos)
  y_pos += 50

# Networth label
ttk.Label(dashboard_tab, text="Net Worth").place(x = 400 - len("Net Worth"), y = 400)
ttk.Label(dashboard_tab, text="Asset").place(x = 200, y = 450)
ttk.Label(dashboard_tab, text="Liablity").place(x = 600, y = 450)

# Asset label
y_pos = 500
for i in range(len(month_asset[0])):
  ttk.Label(dashboard_tab, text=str(month_asset[0][i]) + "\t" + str(month_asset[1][i])).place(x = 200, y = y_pos)
  y_pos += 50

# Liability label
y_pos = 500
for i in range(len(month_liability[0])):
  ttk.Label(dashboard_tab, text=str(month_liability[0][i]) + "\t" + str(month_liability[1][i])).place(x = 600, y = y_pos)
  y_pos += 50

# Income tab label
ttk.Label(income_tab, text=str(month_income[0][i])).place(x = 400, y = 10)
y_pos = 10
for i in range(len(month_income[0])):
  ttk.Label(income_tab, text=str(month_income[0][i]) + "\t" + str(month_income[1][i])).place(x = 40, y = y_pos)
  y_pos += 50

# Expense tab label
ttk.Label(expenses_tab, text=str(month_expenses[0][i]) + "\t" + str(month_expenses[1][i])).place(x = 400, y = 10)
y_pos = 10
for i in range(len(month_expenses[0])):
  ttk.Label(expenses_tab, text=str(month_expenses[0][i]) + "\t" + str(month_expenses[1][i])).place(x = 40, y = y_pos)
  y_pos += 50

# ------------------------------------- dashboard -------------------------------------

def fig_init(width, height, dpi):
  fig = Figure(figsize=(width, height), dpi=dpi)
  ax = fig.add_subplot(111)
  return fig, ax

def save_display(fig, img_name, img_width, img_height):
  fig.savefig('images/' + img_name, transparent=True)
  img = Image.open('images/' + img_name)
  img = img.resize((img_width, img_height), Image.ANTIALIAS)
  return ImageTk.PhotoImage(img)

# summary bar chart 
report_ax = fig_init(5, 5, 100)
report_ax[1].bar(range(len(month_report[0])), month_report[1], align='edge', width=1.0, color=['red', 'blue', 'yellow', 'green'])
report_ax[1].legend(loc = 'upper left')
report_ax[1].set_xlabel('Type')
report_ax[1].set_ylabel('Amount')
summary_bar_img = save_display(report_ax[0], "summary_bar.png", 350, 350)
ttk.Label(dashboard_tab, image = summary_bar_img).place(x = 350, y = 0)

# networth line graph 
networth_ax = fig_init(5, 5, 100)
networth_ax[1].plot(month_index[:-1], [i[0] for i in networth], color= 'orange')
networth_line_img = save_display(networth_ax[0], "networth_line.png", 200, 200)
ttk.Label(dashboard_tab, image = networth_line_img).place(x = 150, y = 500)

# # dashboard report line graph
# report_ax = db_fig.add_subplot(224)
# report_color = ['green', 'red', 'yellow', 'blue']

# for j in range(len(month_report[0])):
#   report_ax.plot(month_index[:-1], [i[1][j] for i in report], color= report_color[j] , label=month_report[0][j])
# report_ax.legend(loc = 'upper left')

# report_fig = FigureCanvasTkAgg(db_fig, dashboard_tab)
# report_fig.get_tk_widget().pack()

# line_ax.title('Net Worth')
# line_ax.xlabel('Month')
# line_ax.plt.ylabel('RM')

# ------------------------------------- income -------------------------------------

# income pie chart
income_fig = Figure(figsize=(3, 3), dpi=100)
income_ax = income_fig.add_subplot(111)
income_ax.pie(month_income[1], radius=1, labels=month_income[0], labeldistance=True, autopct=make_autopct(month_income[1]))
# ax.legend(bbox_to_anchor=(0.5, 0.5), loc='lower left')
income_pie = FigureCanvasTkAgg(income_fig, income_tab)
income_pie.get_tk_widget().pack()

# expenses pie chart
expenses_fig = Figure(figsize=(3,3), dpi=100)
expenses_ax = expenses_fig.add_subplot(111)
expenses_ax.pie(month_expenses[1], radius=1, labels=month_expenses[0], labeldistance=True, autopct=make_autopct(month_expenses[1]))
# ax.legend(bbox_to_anchor=(0.5, 0.5), loc='lower left')
expenses_pie = FigureCanvasTkAgg(expenses_fig, expenses_tab)
expenses_pie.get_tk_widget().pack()

# canvas = Canvas()
# canvas.create_line(15, 25, 200, 25)
# canvas.pack()

if __name__ == "__main__":
  root.mainloop()