#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[6]:


url = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
url


# In[7]:


soup = BeautifulSoup(url.content)


# In[8]:


soup


# In[11]:


res_name = []
for i in soup.find_all('a', class_="restnt-name ellipsis"):
    res_name.append(i.text)


# In[12]:


res_name


# In[13]:


location = []
for i in soup.find_all('div', class_="restnt-loc ellipsis"):
    location.append(i.text)
location


# In[21]:


cuisine = []
for i in soup.find_all('span', class_="double-line-ellipsis"):
    cuisine_name = i.text.split('|')[-1].strip()
    cuisine.append(cuisine_name)
cuisine


# In[24]:


ratings = []
for i in soup.find_all('div', class_="restnt-rating rating-4"):
    ratings.append(i.text)
ratings


# In[32]:


image_url = []
for i in soup.find_all('img', class_="no-img"):
    image_url.append(i.get('data-src'))
image_url


# In[33]:


data = {'Restaurant':res_name, 'Place':location, 'Ratings':ratings, 'Cuisine':cuisine, 'Image_URL':image_url}
df = pd.DataFrame(data)
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




