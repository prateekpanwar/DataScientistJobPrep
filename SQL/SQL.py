# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:56:25 2018

@author: hp1
"""

import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial.db') #create a db
c = conn.cursor() #creating cursor

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffsToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
    
def data_entry():
    c.execute("INSERT INTO stuffsToPlot VALUES(12345665478, '2016-01-01', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()
    
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = "Python"
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffsToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()

def read_from_db():
    #c.execute("SELECT * FROM stuffsToPlot")
    #c.execute("SELECT * FROM stuffsToPlot WHERE value=3 AND keyword='Python'")
    c.execute("SELECT unix, datestamp FROM stuffsToPlot WHERE value=8 AND keyword='Python'")
    #data = c.fetchall()
    #print(data)                    #getting the data all at once
    
    for data in c.fetchall():
        print(data)

def update():
    c.execute("UPDATE stuffsToPlot SET value = 3 WHERE value=8")
    conn.commit()
    c.execute("SELECT * FROM stuffsToPlot WHERE value=3")
    for data in c.fetchall():
        print(data)

def delete():
    c.execute("DELETE FROM stuffsToPlot WHERE value = 3")
    conn.commit()
    
    c.execute("SELECT * FROM stuffsToPlot WHERE value=3")
    for data in c.fetchall():
        print(data)
    
#create_table() #creating a table
#data_entry() #manual entry
#for i in range(20):    
#    dynamic_data_entry() #Automatic entry
#    time.sleep(1)

#read_from_db()
#update()
delete()
c.close()
conn.close()
    