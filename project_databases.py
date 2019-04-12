# Databases

import sqlite3

class Stocks:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        #self.price = price

class Funds:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        #self.price = price

# Inserting values
def insert_stocks(stock):
    with conn: # with conn: is used so that we don't have to commit() everytime
        c.execute("INSERT INTO Stocks VALUES (:name, :quantity)",
                  {'name': stock.name, 'quantity': stock.quantity})

def insert_funds(Funds):
    with conn: # with conn: is used so that we don't have to commit() everytime
        c.execute("INSERT INTO Funds VALUES (:name, :quantity)",
                  {'name': Funds.name, 'quantity': Funds.quantity})
'''
# Delete entry
def delete_Stocks(name, quantity):
    with conn:
        c.execute("DELETE from Stocks WHERE name = :name AND quantity = :quantity",
                  {'name': stock.name, 'quantity': Stocks.quantity})

def delete_Funds(name, quantity):
    with conn:
        c.execute("DELETE from Funds WHERE name = :name AND quantity = :quantity",
                  {'name': Funds.name, 'quantity': Funds.quantity})

# Update Entry
def update_Stocks(name, quantity):
    with conn:
        c.execute("""UPDATE Stocks SET quantity = :pay
                    WHERE name = :name AND quantity = :quantity""",
                  {'first': first, 'last': last,})
'''


conn = sqlite3.connect('miniproject.db') # Connect to Database stored in RAM
c = conn.cursor() # Creating a cursor to execute SQL Commands
'''
c.execute("""CREATE TABLE Stocks (
        name text,
        quantity integer
    )""")

conn.commit()

c.execute("""CREATE TABLE Funds (
        name text,
        quantity integer
    )""")

conn.commit()
'''
