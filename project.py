from tkinter import Tk, Label,OptionMenu,StringVar,Button,Entry,messagebox
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import urllib.request
import requests
import numpy as np
import project_databases as db
import sqlite3

def buttonClick1():
    
    query_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=GOOGL&apikey=RC90TGA5BKPHHRVT"

    response = requests.get(query_url)
    global data
    data = response.json()

    close = []
    dates = []

    for i in data["Time Series (Daily)"]:
        close.append(data["Time Series (Daily)"][i]["4. close"])
        dates.append(i)

    new = []
    close = [float(i) for i in close]
    plt.plot(dates,close)

    plt.xticks([])
    plt.show()

    dialog_title = 'Buy'
    dialog_text = 'Do you want to continue'
    messagebox.askquestion(dialog_title,dialog_text)

    quantity = number.get()
    share = db.Stocks('GOOGLE', quantity)
    db.insert_stocks(share)


##    window1 = Toplevel(root)
##    window1.geometry("860x450+50+50")
##    window1.title("Stock")
##    QUERY_URL = "https://www.alphavantage.co/query?function={REQUEST_TYPE}&symbol={SYMBOL}&apikey={KEY}"
##    API_KEY = "RC90TGA5BKPHHRVT"
##    def _request(symbol,req_type):
##        with urllib.request.urlopen(QUERY_URL.format(REQUEST_TYPE=req_type, KEY=API_KEY, SYMBOL=symbol)) as req:
##            data = req.read().decode("UTF-8")
##        return data
##    def get_daily_data(symbol):
##        return json.loads(_request(symbol,'TIME_SERIES_MONTHLY'))
##    msft = get_daily_data("MSFT")




def buttonClick2():
    window1 = Toplevel(root)
    window1.geometry("860x450+50+50")
    window1.title("Fund Management")
    


root = Tk()

root.title("Stock and mutual fund")
root.geometry("1050x700+50+50")

conn = sqlite3.connect('miniproject.db') # Connect to Database stored in RAM
c = conn.cursor() # Creating a cursor to execute SQL Commands

main_menu = Menu(root, tearoff=0)
main_menu.add_command(label="Buy")
main_menu.add_command(label="Sell")
root.config(menu=main_menu)

label1 = Label(root, text="Stock and mutual fund manager", font="none 24 bold",bg="orange",fg = "White").place(x=230,y=0,width=600,height=40)


label21 = Label(root, text="Stocks", font="none 16 bold",bg="grey",fg = "black").place(x=195,y=55,width=100,height=40)

label22 = Label(root, text="Mutual funds ", font="none 16 bold",bg="grey",fg = "black").place(x=700,y=55,width=150,height=40)

OPTIONS = [
"Microsoft",
"Apple",
"Google"
]


variable1 = StringVar(root)
variable1.set(OPTIONS[0]) # default value

w1 = OptionMenu(root, variable1, *OPTIONS).place(x=195,y=102,width=100,height=40)

variable2 = StringVar(root)
variable2.set(OPTIONS[0]) # default value

w2 = OptionMenu(root, variable2, *OPTIONS).place(x=700,y=102,width=120,height=40)



button1= Button(root, text='Buy',bg = "Green",command=buttonClick1)
button1.place(x = 195,y = 190,width = 120,height = 30)


button2= Button(root, text='Buy',bg = "Green",command=buttonClick2)
button2.place(x = 700,y = 190,width = 120,height = 30)


my_text = Label(root,text="Quantity")
my_text.place(x = 195,y = 150,width = 60,height = 30)

number = StringVar()
E1=Entry(root,bg='white',fg='black',font=('Georgia',10), textvariable = number)
E1.place(x = 255,y = 150,width = 120,height = 30)

label1 = Label(root, text=" CURRENT PORTFOLIO", font="none 24 bold",bg="orange",fg = "White").place(x=230,y=290,width=600,height=40)

tab1_display = ScrolledText(root, height = 10)
tab1_display.grid(columnspan = 2, pady = 3, padx = 5)
tab1_display.place(x = 150,y = 370,width = 730)


labe112 = Label(root, text="Total investment:", font="none 16 bold",bg="grey",fg = "black").place(x=180,y=550,width=180,height=30)
labe122 = Label(root, text="Total investment:", font="none 16 bold",bg="grey",fg = "black").place(x=600,y=550,width=180,height=30)


button11= Button(root, text='Stock Details',bg = "Blue")
button11.place(x = 180,y = 590,width = 150,height = 30)

button21= Button(root, text='Fund Details',bg = "Blue")
button21.place(x = 600,y = 590,width = 150,height = 30)





root.mainloop()
