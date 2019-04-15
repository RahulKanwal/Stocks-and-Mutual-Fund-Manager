import sqlite3
import project_databases as db

conn = sqlite3.connect('miniproject.db')
c = conn.cursor()

c.execute("SELECT * FROM Stocks")
s = c.fetchall()
print(s)
'''
db.insert_portfolio()

db.update_portfolio()

c.execute('SELECT * FROM Portfolio')
r = c.fetchall()
print("r=\n", r)
'''
'''
import project_databases as db
import sqlite3

quantity = number.get()
share = db.Stocks('GOOGLE', quantity)
db.insert_stocks(share)
'''
