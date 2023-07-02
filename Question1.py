#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[20]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[4]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[5]:


page


# In[6]:


soup = BeautifulSoup(page.content)


# In[7]:


soup


# In[23]:


headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])


# In[24]:


header_text = [header.get_text(strip = True) for header in headers]


# In[26]:


df = pd.DataFrame({'Headers': header_text})


# In[27]:


df

