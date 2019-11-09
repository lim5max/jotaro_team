# -*- coding: utf-8 -*-
import sqlite3 as lite

import sys

try:
    con = lite.connect('user.db')
    
    cur = con.cursor()
    cur.execute("CREATE T ABLE user(id INT, name TEXT, birthday TEXT, gender INT, interest INT, idtext INT, like INT)")

except:
    print("error")
# семья, красота, здоровье, авто, недвижимость, психология, коты, собаки, туризм, обучение, юмор, финансы, магия, кулинария, дети, эзотерика
# 1 - 16
