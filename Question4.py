#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[3]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')


# In[4]:


soup = BeautifulSoup(page.content)


# In[5]:


table = soup.find('table', class_='table')


# In[6]:


teams = []
matches = []
points = []
ratings = []


# In[7]:


rows = table.find_all('tr')
for row in rows[1:11]:
    cells = row.find_all('td')
    team = cells[1].text.strip()
    match = cells[2].text.strip()
    point = cells[3].text.strip()
    rating = cells[4].text.strip()
    teams.append(team)
    matches.append(match)
    points.append(point)
    ratings.append(rating)


# In[8]:


data = {'Team': teams, 'Matches': matches, 'Points': points, 'Rating': ratings}
df = pd.DataFrame(data)


# In[9]:


df


# In[10]:


url2 = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')


# In[12]:


soup = BeautifulSoup(url2.content)


# In[13]:


table2 = soup.find('table', class_='table')


# In[14]:


player_name = []
team_name = []
ratings = []


# In[15]:


rows = table2.find_all('tr')
for row in rows[1:11]:
    cells = row.find_all('td')
    player = cells[1].text.strip()
    team = cells[2].text.strip()
    rating = cells[3].text.strip()
    player_name.append(player)
    team_name.append(team)
    ratings.append(rating)


# In[16]:


data2 = {'Player':player_name, 'Team':team_name, 'Rating':ratings}


# In[19]:


df2 = pd.DataFrame(data2)


# In[20]:


df2


# In[21]:


url3 = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/bowling')


# In[29]:


soup = BeautifulSoup(url3.content)


# In[30]:


table3 = soup.find('table', class_='table')


# In[31]:


playeR_name = []
teaM_name = []
ratingS = []


# In[32]:


rows = table3.find_all('tr')
for row in rows[1:11]:
    cells = row.find_all('td')
    player = cells[1].text.strip()
    team = cells[2].text.strip()
    rating = cells[3].text.strip()
    playeR_name.append(player)
    teaM_name.append(team)
    ratingS.append(rating)


# In[33]:


data3 = {'Player':playeR_name, 'Team':teaM_name, 'Rating':ratingS}


# In[34]:


df3 = pd.DataFrame(data3)


# In[35]:


df3


# In[ ]:





# In[ ]:




