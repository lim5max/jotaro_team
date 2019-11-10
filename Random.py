#!/usr/bin/env python
# coding: utf-8

# In[259]:


name = "Ivan"


# In[260]:


age = int(29) 


# In[261]:


interest = int(9)


# In[262]:


gender = int(0)


# In[263]:


import datetime #подтягиваем текущую дату и преобразуем в строку
today= datetime.date.today()
today = str(today.isoformat())
  


# In[264]:


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'): #функция преобразования в бинарный код
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


# In[265]:


bytetext = int(text_to_bits(name)) #преобразуем имя и дату в бинарный код
today = int(text_to_bits(today))


# In[266]:


solt = str((bytetext+today)*age*interest+gender) #конструируем соль из набора данных
solt


# In[267]:


if int(solt[3:6]) <= 300:  #соль, срез трехзначного числа, если больше числа строк, режем до двухзначного
    solt = int(solt[3:6]) 
else: 
    solt = int(solt[3:5])
solt


# In[268]:


import random #функция рандомного числа с солью
x1 = abs(random.randint(1,300)-solt)
x2 = abs(random.randint(1,300)-solt)
x3 = abs(random.randint(1,300)-solt)
x1, x2, x3


# In[ ]:





# In[ ]:




