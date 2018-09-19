# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:56:25 2018

@author: hp1
"""

import sqlite3

conn = sqlite3.connect('tutorial.db') #create a db
c = conn.cursor() #creating cursor

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffsToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
    
def data_entry():
    c.execute("INSERT INTO stuffsToPlot VALUES(12345678, '2016-01-01', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()
    
create_table()
data_entry()