#!/usr/bin/env python
# coding: utf-8

# In[55]:


name = "Ivan"


# In[56]:


age = int(29) 


# In[57]:


interest = int(9)


# In[58]:


#gender = int(0)
rows = int(300)


# In[59]:


import datetime #подтягиваем текущую дату и преобразуем в строку
today= datetime.date.today()
today = str(today.isoformat())
  


# In[60]:


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'): #функция преобразования в бинарный код
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


# In[61]:


bytetext = int(text_to_bits(name)) #преобразуем имя и дату в бинарный код
today = int(text_to_bits(today))


# In[62]:


solt = str((bytetext+today)*age*interest) #конструируем соль из набора данных
solt


# In[63]:


if int(solt[3:6]) <= rows:  #соль, срез трехзначного числа, если больше числа строк, режем до двухзначного
    solt = int(solt[3:6]) 
else: 
    solt = int(solt[3:5])
solt


# In[87]:


solt=98
part1=rows-solt+1
if abs(int(str(solt*solt*solt)[:3]))<=rows:
    part2=abs(int(str(solt*solt*solt)[:3]))
else: part2=abs(int(str(solt*solt*solt)[:2]))

if abs(int(str(rows-2*solt)))<=rows:
    part3=abs(int(str(rows-2*solt)))
else: part3=int(str(rows-2*solt)[:2])
part1,part2,part3


# In[12]:


import random #функция рандомного числа с солью
x1 = abs(random.randint(1,rows)-solt)
x2 = abs(random.randint(1,rows)-solt)
x3 = abs(random.randint(1,rows)-solt)
x1, x2, x3


# In[ ]:





# In[ ]:




