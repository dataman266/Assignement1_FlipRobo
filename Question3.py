#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[4]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# In[5]:


soup = BeautifulSoup(page.content)


# In[6]:


soup


# In[7]:


team_name = soup.find_all('span' , class_="u-hide-phablet")
team_name


# In[9]:


team_names = []


# In[10]:


for i in team_name:
    team_names.append(i.text.strip())


# In[11]:


print(team_names)


# In[15]:


table = soup.find('table', class_='table')


# In[16]:


teams = []
matches = []
points = []
ratings = []


# In[17]:


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


# In[18]:


data = {'Team': teams, 'Matches': matches, 'Points': points, 'Rating': ratings}
df = pd.DataFrame(data)


# In[19]:


df


# In[20]:


url = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')


# In[21]:


soup = BeautifulSoup(url.content)


# In[22]:


soup


# In[24]:


table2 = soup.find('table', class_='table')


# In[26]:


player_name = []
team_name = []
ratings = []


# In[27]:


rows = table2.find_all('tr')
for row in rows[1:11]:
    cells = row.find_all('td')
    player = cells[1].text.strip()
    team = cells[2].text.strip()
    rating = cells[3].text.strip()
    player_name.append(player)
    team_name.append(team)
    ratings.append(rating)


# In[29]:


data2 = {'Player':player_name, 'Team':team_name, 'Rating':ratings}


# In[30]:


df2 = pd.DataFrame(data)


# In[31]:


df2


# In[48]:


url2 = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')


# In[49]:


soup = BeautifulSoup(url2.content)


# In[50]:


soup


# In[51]:


table3 = soup.find('table', class_='table')


# In[53]:


playeR_name = []
teaM_name = []
ratingS = []


# In[54]:


rows = table3.find_all('tr')
for row in rows[1:11]:
    cells = row.find_all('td')
    player = cells[1].text.strip()
    team = cells[2].text.strip()
    rating = cells[3].text.strip()
    playeR_name.append(player)
    teaM_name.append(team)
    ratingS.append(rating)


# In[55]:


data3 = {'Player':playeR_name, 'Team':teaM_name, 'Rating':ratingS}


# In[58]:


df3 = pd.DataFrame(data3)


# In[59]:


df3


# In[ ]:




