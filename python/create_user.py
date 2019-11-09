# -*- coding: utf-8 -*-
import sqlite3 as lite

import sys

try:
    con = lite.connect('user.db')
    
    cur = con.cursor()
    cur.execute("CREATE TABLE user(id INT, name TEXT, birthday TEXT, gender INT, interest INT, idtext INT, like INT)")
    
except:
    print("error")