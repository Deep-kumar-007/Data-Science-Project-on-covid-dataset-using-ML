#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as  pd
import seaborn as sns


# In[15]:


dataset = pd.read_csv("Covid StatewiseTestingDetails.csv")


# In[16]:


dataset.columns


# In[17]:


type(dataset)


# In[18]:


dataset


# In[19]:


dataset.isnull()


# In[20]:


sns.heatmap(  dataset.isnull() )


# In[ ]:





# In[ ]:





# In[ ]:





# In[12]:


import pandas as pd

df = pd.DataFrame({
    "Date": pd.to_datetime(["2023-02-16", "2023-02-17", "2023-02-18", "2023-02-19", "2023-02-20"]),
    "Total Cases": [10751, 10622, 10503, 10384, 10265],
    "Active Cases": [129, 117, 105, 93, 81],
    "Recovered Cases": [10622, 10503, 10384, 10265, 10184],
    "Deaths": [125, 117, 110, 103, 99]
})

df["Daily Increase"] = df["Total Cases"] - df["Total Cases"].shift(1)

df["7-day Moving Average"] = df["Total Cases"].rolling(7).mean()

df.plot(x="Date", y="Total Cases")

df.plot(x="Date", y="Daily Increase")

df.plot(x="Date", y="7-day Moving Average")

df.to_csv("covid_andaman_nicobar_islands.csv")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




