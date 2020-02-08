#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd


# In[51]:


#First four elements are fake
data = [[0,'H','80-89',2],[1,'H','60-69',1],[2,'D','80-89',1],[3,'H','90+',2]]
voluntaris = pd.DataFrame(data,columns=['Id','Sexe','FranjaEdat','NumVoluntariats'],dtype=int)

voluntaris.head()


# In[47]:


#Add an element when signing up
from jutge import read
columnes=['Id','Sexe','FranjaEdat','NumVoluntariats']

#read element
sexe = 'H'
edat = 64
num_voluntariats = 2

def franja_edat(edat):
    if edat<70:
        return '60-69'
    elif edat<80:
        return '70-79'
    elif edat<90:
        return '80-89'
    else:
        return '90+'
    
voluntari = pd.DataFrame([voluntaris.tail(1).index[0]+1, sexe, franja_edat(edat), num_voluntariats], columnes)

voluntaris = voluntaris.pd.concat(voluntari)


# 

# In[52]:


voluntaris.to_csv('llista_voluntaris.csv', sep='\t')


# In[ ]:





# In[ ]:




