#!/usr/bin/env python
# coding: utf-8
import sys
name = sys.argv[0]

age = sys.argv[1]
interest = sys.argv[2]

#gender = int(0)
rows = int(200)

import datetime #подтягиваем текущую дату и преобразуем в строку
today= datetime.date.today()
today = str(today.isoformat())

bytetext = int.from_bytes(bytes(name, encoding="utf-8"),  byteorder='big')

today = int.from_bytes(bytes(today, encoding="utf-8"),  byteorder='big')

solt = str((bytetext+today)*age*interest) #конструируем соль из набора данных

if int(solt[3:6]) <= rows:  #соль, срез трехзначного числа, если больше числа строк, режем до двухзначного
    solt = int(solt[3:6]) 
else: 
    solt = int(solt[3:5])

part1=rows-solt+1
if abs(int(str(solt*solt*solt)[:3]))<=rows:
    part2=abs(int(str(solt*solt*solt)[:3]))
else: part2=abs(int(str(solt*solt*solt)[:2]))

if abs(int(str(rows-2*solt)))<=rows:
    part3=abs(int(str(rows-2*solt)))
else: part3=int(str(rows-2*solt)[:2])


import random #функция рандомного числа с солью
x1 = abs(random.randint(1,rows)-solt)
x2 = abs(random.randint(1,rows)-solt)
x3 = abs(random.randint(1,rows)-solt)

file  = open('./json/text.json', 'r')
a = ""
for (i, index) in file.readlines():
    if index == x1:
        a+=i
    elif index == x2:
        a+=i
    elif index == x3:
        a+=i

file.close()
print(a)
sys.stdout.flush()