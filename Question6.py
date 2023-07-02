#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[17]:


from bs4 import BeautifulSoup
import pandas as pd
import requests


# In[18]:


url = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[19]:


soup = BeautifulSoup(url.content)


# In[26]:


article_name = soup.find('h2', class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg")
article_name


# In[30]:


paper = []
for i in soup.find_all('h2', class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    paper.append(i.text)
    


# In[31]:


paper


# In[32]:


author = []
for i in soup.find_all('span', class_="sc-1w3fpd7-0 dnCnAO"):
    author.append(i.text)


# In[33]:


author


# In[34]:


date = []
for i in soup.find_all('span', class_="sc-1thf9ly-2 dvggWt"):
    date.append(i.text)


# In[35]:


date


# In[40]:


paper_urls = []
for link in soup.find_all('a', class_='article-content-title u-margin-top-xs'):
    paper_urls.append(link['href'])

paper_urls


# In[39]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




