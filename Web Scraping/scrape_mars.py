# Dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd


def init_browser():

    #executable_path = {"executable_path": "chromedriver"}
    #return Browser("chrome", **executable_path, headless=False)
    executable_path = {'executable_path': 'chromedriver'}
    return Browser('chrome', headless=True, **executable_path)



## NASA MARS NEWS ##

mars_data = {}

def scrape_mars_data_news():
    browser = init_browser()

    try:

# Initialize browser
        #browser = init_browser()

# URL of page to be scraped
        url = 'https://mars.nasa.gov/news'
        browser.visit(url)
# Retrieve page with the requests module
        response = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
        soup = bs(response.text, 'html.parser')

# Retrieve news title and paragraph description
        results_title = soup.find(class_='content_title')
        news_title = results_title.text.strip()

        results_news_description = soup.find(class_='rollover_description_inner')
        news_p = results_news_description.text.strip()

# Entry retrieve data into dictionary
        mars_data['news_title'] = news_title
        mars_data['results_paragraph'] = news_p

        return mars_data
    
    finally:
        browser.quit()



## JPL MARS SPACE IMAGES ##

mars_images = {}

def scrape_mars_images():

# Initialize browser
    browser = init_browser()

    try:

# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
        #get_ipython().system('which chromedriver')

        images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(images_url)

        html = browser.html
        soup = bs(html, 'html.parser')

# Retrieve data from site
        mars_images_results = soup.find_all(class_='articles')

        slide_image__result = soup.find(class_='slide')

        data_fancybox_url_result = soup.find_all('a',class_='fancybox')[1].get('data-fancybox-href')

        base_url = 'https://www.jpl.nasa.gov'
        feature_image_url = base_url + data_fancybox_url_result
        feature_image_url

# Entry retrieve data into dictionary
        mars_images['feature_image_url'] = feature_image_url

        return mars_images
    
    finally: 
        browser.quit()



## MARS WEATHER ##

mars_weather = {}

def scrape_mars_weather():

# Initialize browser
    browser = init_browser()

    try:

# URL of page to be scraped
        weather_url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(weather_url)

# Retrieve page with the requests module
        response = requests.get(weather_url)

# Create BeautifulSoup object; parse with 'html.parser'
        soup = bs(response.text, 'html.parser')

        mars_weather_content = soup.find(class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')

        mars_weather_result = mars_weather_content.text.strip()
    
# Entry retrieve data into dictionary
        mars_weather['mars_weather_result'] = mars_weather_result
       
        return mars_weather
    
    finally: 
        browser.quit()



## MARS FACTS ##

mars_facts = {}

def scrape_mars_facts():

    # Initialize browser
    browser = init_browser()

    try:

# URL of page to be scraped
        facts_url = 'https://space-facts.com/mars/'


        tables = pd.read_html(facts_url)

        df = tables[0]
        df.columns = ['Planet Facts','Results']

        df.set_index('Planet Facts', inplace=True)

        html_table = df.to_html()
        html_table_string = html_table.replace('\n', '')
    
# Entry retrieve data into dictionary
        mars_facts['mars_facts_table'] = html_table_string

        return mars_facts

    finally: 
        browser.quit()



## MARS HEMISPHERES ##

mars_hemispheres = []

def scrape_mars_hemispheres():

    # Initialize browser
    browser = init_browser()

    try:
        
# URL of page to be scraped
        hemispheres_1_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
        browser.visit(hemispheres_1_url)

# Retrieve page with the requests module
        response = requests.get(hemispheres_1_url)

# Create BeautifulSoup object; parse with 'html.parser'
        soup = bs(response.text, 'html.parser')

        url_cerberus = soup.find(target='_blank')
        url_cerberus = url_cerberus.get('href')

        title_cerberus = soup.find('h2', class_='title').text
    
        hemisphere_list_1 = {'title': title_cerberus, 'image_url': url_cerberus}

# URL of page to be scraped
        hemispheres_2_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
        browser.visit(hemispheres_2_url)

# Retrieve page with the requests module
        response = requests.get(hemispheres_2_url)

# Create BeautifulSoup object; parse with 'html.parser'
        soup = bs(response.text, 'html.parser')

        url_schiaparelli = soup.find(target='_blank')
        url_schiaparelli = url_schiaparelli.get('href')

        title_schiaparelli = soup.find('h2', class_='title').text

        hemisphere_list_2 = {'title': title_schiaparelli, 'image_url': url_schiaparelli}

# URL of page to be scraped
        hemispheres_3_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
        browser.visit(hemispheres_3_url)

# Retrieve page with the requests module
        response = requests.get(hemispheres_3_url)

# Create BeautifulSoup object; parse with 'html.parser'
        soup = bs(response.text, 'html.parser')

        url_syrtis_major = soup.find(target='_blank')
        url_syrtis_major = url_syrtis_major.get('href')

        title_syrtis_major = soup.find('h2', class_='title').text

        hemisphere_list_3 = {'title': title_syrtis_major, 'image_url': url_syrtis_major}

# URL of page to be scraped
        hemispheres_4_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

# Retrieve page with the requests module
        response = requests.get(hemispheres_4_url)
        browser.visit(hemispheres_4_url)

# Create BeautifulSoup object; parse with 'html.parser'
        soup = bs(response.text, 'html.parser')

        url_valles_marineris = soup.find(target='_blank')
        url_valles_marineris = url_valles_marineris.get('href')
    

        title_valles_marineris = soup.find('h2', class_='title').text

        hemisphere_list_4 = {'title': title_valles_marineris, 'image_url': url_valles_marineris}

        mars_hemispheres.append(hemisphere_list_1)
        mars_hemispheres.append(hemisphere_list_2)
        mars_hemispheres.append(hemisphere_list_3)
        mars_hemispheres.append(hemisphere_list_4)

        return mars_hemispheres

    finally:
        browser.quit()

    