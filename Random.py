#!/usr/bin/env python
# coding: utf-8

# In[195]:


name = "Ivan"


# In[196]:


age = int(29) 


# In[197]:


interest = int(9)


# In[198]:


gender = int(0)


# In[199]:


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


# In[200]:


bytetext = int(text_to_bits(name))


# In[201]:


text_to_bits(name)


# In[202]:


solt = str(bytetext*age*interest+gender)
solt


# In[203]:


if int(solt[3:6]) <= 300:  #соль, срез трехначного числа, если больше числа строк, режем до двухзначного
    solt = int(solt[3:6]) 
else: 
    solt = int(solt[3:5])
solt


# In[204]:


import random #функция рандомного числа с солью
x1 = abs(random.randint(1,300)-solt)
x2 = abs(random.randint(1,300)-solt)
x3 = abs(random.randint(1,300)-solt)
x1, x2, x3


# In[ ]:





# In[ ]:




