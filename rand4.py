#!/usr/bin/env python
# coding: utf-8

# In[167]:


name = "Ivan"


# In[168]:


age = int(29) 


# In[169]:


interest = int(9)


# In[170]:


#gender = int(0)
rows = int(300)


# In[171]:


import datetime #подтягиваем текущую дату и преобразуем в строку
today= datetime.date.today()
today = str(today.isoformat())
today


# In[172]:


#def text_to_bits(text, encoding='utf-8', errors='surrogatepass'): #функция преобразования в бинарный код
  #  bits = bin(int.from_bytes(text.encode(encoding, errors)), 'big'))[2:]
   # return bits.zfill(8 * ((len(bits) + 7) // 8))
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


# In[173]:


bytetext = int(text_to_bits(name)) #преобразуем имя и дату в бинарный код
today = int(text_to_bits(today))
bytetext
today


# In[174]:


solt = str((bytetext+today)*age*interest) #конструируем соль из набора данных


# In[175]:


if int(solt[3:6]) <= rows:  #соль, срез трехзначного числа, если больше числа строк, режем до двухзначного
    solt = int(solt[3:6]) 
else: 
    solt = int(solt[3:5])


# In[176]:



part1=rows-solt+1
if abs(int(str(solt*solt*solt)[:3]))<=rows:
    part2=abs(int(str(solt*solt*solt)[:3]))
else: part2=abs(int(str(solt*solt*solt)[:2]))

if abs(int(str(rows-2*solt)))<=rows:
    part3=abs(int(str(rows-2*solt)))
else: part3=int(str(rows-2*solt)[:2])


# In[177]:


import random #функция рандомного числа с солью
x1 = abs(random.randint(1,rows)-solt)
x2 = abs(random.randint(1,rows)-solt)
x3 = abs(random.randint(1,rows)-solt)


# In[178]:


x1,x2,x3


# In[179]:


part1


# In[ ]:




