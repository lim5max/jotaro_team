name = "Ivan"
age = int(29) 
interest = int(9)
gender = int(0)

import datetime #подтягиваем текущую дату и преобразуем в строку
today= datetime.date.today()
today = str(today.isoformat())

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'): #функция преобразования в бинарный код
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

bytetext = int(text_to_bits(name)) #преобразуем имя и дату в бинарный код
today = int(text_to_bits(today))

solt = str((bytetext+gender+today)*age*interest) #конструируем соль из набора данных

if int(solt[3:6]) <= 300:  #соль, срез трехзначного числа, если больше числа строк, режем до двухзначного
    solt = int(solt[3:6]) 
else: 
    solt = int(solt[3:5])

import random #функция рандомного числа с солью
x1 = abs(random.randint(1,300)-solt)
x2 = abs(random.randint(1,300)-solt)
x3 = abs(random.randint(1,300)-solt)

