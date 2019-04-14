#!/usr/bin/env python
# coding: utf-8

# In[32]:


# Dependencies
from bs4 import BeautifulSoup as bs
import requests


# In[33]:


## NASA MARS NEWS ##


# In[34]:


# URL of page to be scraped
url = 'https://mars.nasa.gov/news'


# In[35]:


# Retrieve page with the requests module
response = requests.get(url)


# In[36]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(response.text, 'html.parser')


# In[37]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[38]:


results_title = soup.find(class_='content_title')
print(results_title)


# In[39]:


news_title = results_title.text.strip()
news_title


# In[40]:


results_news_description = soup.find(class_='rollover_description_inner')
print(results_news_description)


# In[41]:


news_p = results_news_description.text.strip()
news_p


# In[ ]:





# In[ ]:


## JPL MARS SPACE IMAGES ##


# In[42]:


# Dependencies
from splinter import Browser


# In[43]:


# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
get_ipython().system('which chromedriver')


# In[44]:


executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[45]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[46]:


html = browser.html
soup = bs(html, 'html.parser')


# In[47]:


print(soup.prettify())


# In[48]:


mars_images_results = soup.find_all(class_='articles')
print(mars_images_results)


# In[49]:


slide_image__result = soup.find(class_='slide')
print(slide_image__result)


# In[50]:


data_fancybox_url_result = soup.find_all('a',class_='fancybox')[1].get('data-fancybox-href')
print(data_fancybox_url_result)


# In[51]:


base_url = 'https://www.jpl.nasa.gov'
feature_image_url = base_url + data_fancybox_url_result
feature_image_url


# In[ ]:





# In[ ]:


## MARS WEATHER ##


# In[52]:


# URL of page to be scraped
url = 'https://twitter.com/marswxreport?lang=en'


# In[53]:


# Retrieve page with the requests module
response = requests.get(url)


# In[54]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(response.text, 'html.parser')


# In[55]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[57]:


mars_weather_content = soup.find(class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
print(mars_weather_content)


# In[58]:


mars_weather = mars_weather_content.text.strip()
print(mars_weather)


# In[ ]:





# In[ ]:


## MARS FACTS ##


# In[59]:


import pandas as pd


# In[60]:


url = 'https://space-facts.com/mars/'


# In[61]:


tables = pd.read_html(url)
tables


# In[62]:


type(tables)


# In[63]:


df = tables[0]
df.columns = ['Planet Facts','Results']
df.head(10)


# In[64]:


df.set_index('Planet Facts', inplace=True)
df.head(10)


# In[65]:


html_table = df.to_html()
html_table


# In[66]:


html_table_string = html_table.replace('\n', '')
html_table_string


# In[ ]:





# In[ ]:


## MARS HEMISPHERES ##


# In[67]:


# URL of page to be scraped
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'


# In[68]:


# Retrieve page with the requests module
response = requests.get(url)


# In[69]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(response.text, 'html.parser')


# In[70]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[71]:


url_cerberus = soup.find(target='_blank')
url_cerberus = url_cerberus.get('href')
print(url_cerberus)


# In[72]:


title_cerberus = soup.find('h2', class_='title').text
print(title_cerberus)


# In[ ]:





# In[73]:


# URL of page to be scraped
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'


# In[74]:


# Retrieve page with the requests module
response = requests.get(url)


# In[75]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(response.text, 'html.parser')


# In[76]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[78]:


url_schiaparelli = soup.find(target='_blank')
url_schiaparelli = url_schiaparelli.get('href')
print(url_schiaparelli)


# In[79]:


title_schiaparelli = soup.find('h2', class_='title').text
print(title_schiaparelli)


# In[ ]:





# In[80]:


# URL of page to be scraped
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'


# In[81]:


# Retrieve page with the requests module
response = requests.get(url)


# In[82]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(response.text, 'html.parser')


# In[83]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[84]:


url_syrtis_major = soup.find(target='_blank')
url_syrtis_major = url_syrtis_major.get('href')
print(url_syrtis_major)


# In[85]:


title_syrtis_major = soup.find('h2', class_='title').text
print(title_syrtis_major)


# In[ ]:





# In[86]:


# URL of page to be scraped
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'


# In[87]:


# Retrieve page with the requests module
response = requests.get(url)


# In[88]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(response.text, 'html.parser')


# In[89]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[91]:


url_valles_marineris = soup.find(target='_blank')
url_valles_marineris = url_valles_marineris.get('href')
print(url_valles_marineris)


# In[92]:


title_valles_marineris = soup.find('h2', class_='title').text
print(title_valles_marineris)


# In[ ]:





# In[94]:


hemisphere_image_urls = [
    {"title": title_cerberus, "image_url": url_cerberus},
    {"title": title_schiaparelli, "image_url": url_schiaparelli},
    {"title": title_syrtis_major, "image_url": url_syrtis_major},
    {"title": title_valles_marineris, "image_url": url_valles_marineris}
]


# In[95]:


hemisphere_image_urls


# In[96]:


type(hemisphere_image_urls)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




