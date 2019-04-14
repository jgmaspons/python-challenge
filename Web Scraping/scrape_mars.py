# Dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd


def scrape():

## NASA MARS NEWS ##

# URL of page to be scraped
    url = 'https://mars.nasa.gov/news'

# Retrieve page with the requests module
    response = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')

    results_title = soup.find(class_='content_title')

    news_title = results_title.text.strip()

    results_news_description = soup.find(class_='rollover_description_inner')

    news_p = results_news_description.text.strip()


## JPL MARS SPACE IMAGES ##

# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
    get_ipython().system('which chromedriver')

    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    mars_images_results = soup.find_all(class_='articles')

    slide_image__result = soup.find(class_='slide')

    data_fancybox_url_result = soup.find_all('a',class_='fancybox')[1].get('data-fancybox-href')

    base_url = 'https://www.jpl.nasa.gov'
    feature_image_url = base_url + data_fancybox_url_result



## MARS WEATHER ##

# URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'

# Retrieve page with the requests module
    response = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')

    mars_weather_content = soup.find(class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')

    mars_weather = mars_weather_content.text.strip()


## MARS FACTS ##


    url = 'https://space-facts.com/mars/'

    tables = pd.read_html(url)

    df = tables[0]
    df.columns = ['Planet Facts','Results']

    df.set_index('Planet Facts', inplace=True)

    html_table = df.to_html()

    html_table_string = html_table.replace('\n', '')


## MARS HEMISPHERES ##

# URL of page to be scraped
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'

# Retrieve page with the requests module
    response = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')

    url_cerberus = soup.find(target='_blank')
    url_cerberus = url_cerberus.get('href')

    title_cerberus = soup.find('h2', class_='title').text

# URL of page to be scraped
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'

# Retrieve page with the requests module
    response = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')

    url_schiaparelli = soup.find(target='_blank')
    url_schiaparelli = url_schiaparelli.get('href')

    title_schiaparelli = soup.find('h2', class_='title').text

# URL of page to be scraped
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'

# Retrieve page with the requests module
    response = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')

    url_syrtis_major = soup.find(target='_blank')
    url_syrtis_major = url_syrtis_major.get('href')

    title_syrtis_major = soup.find('h2', class_='title').text

# URL of page to be scraped
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

# Retrieve page with the requests module
    response = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')

    url_valles_marineris = soup.find(target='_blank')
    url_valles_marineris = url_valles_marineris.get('href')

    title_valles_marineris = soup.find('h2', class_='title').text

    hemisphere_image_urls = [
        {"title": title_cerberus, "image_url": url_cerberus},
        {"title": title_schiaparelli, "image_url": url_schiaparelli},
        {"title": title_syrtis_major, "image_url": url_syrtis_major},
        {"title": title_valles_marineris, "image_url": url_valles_marineris}
    ]

    return data
