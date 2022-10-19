#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


#Create a series:
birthdays = [2, 3, 8]
years = [2020, 2021, 2022]
series = pd.Series(birthdays, index = years)


# In[6]:


#show series
print(series)


# In[7]:


#Create a series from a dictionary
oscars = {
    1994: ['Tom Hardy', 'NPH'],
    1995: 'Leonardo diCaprio',
    1996: 'Henry Cavill'
}

series = pd.Series(oscars)


# In[8]:


#show series
print(series)


# In[10]:


#You can operate over a series with an array of the same length:

series3 = pd.Series({
    0: 10,
    1: 20,
    2: 30,
    3: 40
})

series4 = pd.Series([
    2,
    3,
    4,
    5
])

sum = series3 + series4
mult = series3 * series4


# In[11]:


print(sum)


# In[12]:


print(mult)


# In[16]:


#DATAFRAMES: 2D data structure
series_by_person = {
    'people': pd.Series(['Andrea', 'Daniel', 'Adrian']),
    'films': pd.Series([['Stranger Things', 'Peaky Blinders'], 'The Good Place', ['The Mole','The Magicians', 'Bridgerton']])
}

df1 = pd.DataFrame(series_by_person)


# In[17]:


print(df1)


# In[18]:


#more easily done with a dict of keys (same ones) and values

my_dict_list =[ {
    'a': 2,
    'b': 3,
    'c': 56,
    'e': 45
    },
    {
    'a': 4,
    'b': 2,
    'd': 12,
    'e': 4,
    'f': 23
    }
]


# In[19]:


df2 = pd.DataFrame(my_dict_list)
    
print(df2) #Observe how keys without values return NaN


# In[ ]:


#Commands to extract data from files:

#From .csv --> pd.read_csv(csv_path)
#From .xlsx --> pd_read_excel(xlsx_path)

