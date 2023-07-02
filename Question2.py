#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')

from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')
soup = BeautifulSoup(page.content, 'html.parser')

name_list = soup.find_all('div', class_="presidentListing")
names = []
terms_of_office = []

for a in name_list:
    president_name = a.find('h3').text.strip()
    term_of_office = a.find('p').text.strip()
    names.append(president_name)
    terms_of_office.append(term_of_office)

df = pd.DataFrame({'Name': names, 'Terms_of_office': terms_of_office})
df


# In[3]:


df

