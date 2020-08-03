# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
from datetime import datetime
import requests

def scrape_all():
    # Initialize headless driver for deployment
    executable_path={'executable_path': '/usr/local/bin/chromedriver'}
    browser=Browser('chrome', 'chromedriver.exe', headless=True)
    news_title, news_p=mars_news(browser)
    cerb_img_url, cerberus_title=cerberus(browser)
    schiap_img_url, schiap_title=schiaparelli(browser)
    syrtis_img_url, syrtis_title=syrtis(browser)
    valles_img_url, valles_title=valles(browser)
    
    # Run all scraping functions and store results in dictionary
    data = {
        'news_title': news_title,
        'news_paragraph': news_p,
        'featured_image': featured_image(browser),
        'facts': mars_facts(),
        # Add new data for challenge
        'cerberus_img': cerb_img_url, 
        'cerberus_title': cerberus_title,
        'schiaparelli_img': schiap_img_url, 
        'schiaparelli_title': schiap_title,
        'syrtis_img': syrtis_img_url, 
        'syrtis_title': syrtis_title,
        'valles_img': valles_img_url, 
        'valles_title': valles_title,
        'last_modified': dt.datetime.now()
    }
    print(data)
    browser.quit()
    return data

# Create function for scraping Mars news from NASA
def mars_news(browser):

    # Visit the mars nasa news site
    url='https://mars.nasa.gov/news/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css('ul.item_list li.slide', wait_time=1)

    # Convert the browser html to a soup object
    html=browser.html
    news_soup=BeautifulSoup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem=news_soup.select_one('ul.item_list li.slide')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title=slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p=slide_elem.find('div', class_='article_teaser_body').get_text()
       
    except AttributeError:
        return None, None

    return news_title, news_p

### Featured Images

def featured_image(browser):

    # Visit URL
    url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem=browser.find_by_id('full_image')
    full_image_elem.click()
    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem=browser.find_link_by_partial_text('more info')
    more_info_elem.click()
    # Parse the resulting html with soup
    html=browser.html
    img_soup=BeautifulSoup(html, 'html.parser')
    # Find the relative image url
    img_url_rel=img_soup.select_one('figure.lede a img').get('src')
    # Use the base URL to create an absolute URL
    img_url=f'https://www.jpl.nasa.gov{img_url_rel}'

    try:
        # Find the relative image url
        img_url_rel=img_soup.select_one('figure.lede a img').get('src')

    except AttributeError:
        return None

    return img_url

def mars_facts():

    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df=pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None
    # Assign columns and set index of dataframe
    df.columns=['Description','Mars']
    df.set_index('Description', inplace=True)
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()

# Challenge 

# Fuction for Cerberus Hemisphere
def cerberus(browser):
    
    # Visit cerberus URL
    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Find and click the Hemisphere link
    cerb_image=browser.find_by_text('Cerberus Hemisphere Enhanced', wait_time=1)
    cerb_image.click()
    # Parse the resulting html with soup
    html=browser.html
    img_soup=BeautifulSoup(html, 'html.parser')
    cerb_soup=BeautifulSoup(html, 'html.parser')
    # Find the title
    cerberus_title=cerb_soup.find("h2", class_='title').get_text()
    cerberus_sample=browser.links.find_by_partial_text('Sample')
    cerberus_sample.click()
    # Find the relative image url
    cerb_url_rel=cerb_soup.select_one('img.wide-image').get('src')
    # Use the base URL to create an absolute URL
    cerb_img_url=f'https://astrogeology.usgs.gov{cerb_url_rel}'
        
    try:
        cerberus_title=cerb_soup.find("h2", class_='title').get_text()
        cerb_url_rel=img_soup.select_one('img.wide-image').get('src')

    except AttributeError:
        return None, None

    return cerb_img_url, cerberus_title

# Fuction for Schiaparelli Hemisphere
def schiaparelli(browser):

    # Visit schiaparelli URL
    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    
    # Find and click the Hemisphere link
    schiap_image=browser.find_by_text('Schiaparelli Hemisphere Enhanced')
    schiap_image.click()
    # Parse the resulting html with soup
    html=browser.html
    img_soup=BeautifulSoup(html, 'html.parser')
    schiap_soup=BeautifulSoup(html, 'html.parser')
    # Find the title
    schiap_title=schiap_soup.find("h2", class_='title').get_text()
    schiaparelli=browser.links.find_by_partial_text('Sample')
    schiaparelli.click()
    # Find the relative image url
    schiap_url_rel=img_soup.select_one('img.wide-image').get('src')
    # Use the base URL to create an absolute URL
    schiap_img_url=f'https://astrogeology.usgs.gov{schiap_url_rel}'

    try:
        schiap_title=schiap_soup.find("h2", class_='title').get_text()
        schiap_url_rel=img_soup.select_one('img.wide-image').get('src')

    except AttributeError:
        return None, None

    return schiap_img_url, schiap_title

# Fuction for Syrtis Major Hemisphere
def syrtis(browser):

    # Visit Syrtis Major URL
    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Find and click the Hemisphere link
    syrtis_image=browser.find_by_text('Syrtis Major Hemisphere Enhanced')
    syrtis_image.click()
    # Parse the resulting html with soup
    html = browser.html
    img_soup=BeautifulSoup(html, 'html.parser')
    syrtis_soup=BeautifulSoup(html, 'html.parser')
    # Find the title
    syrtis_title=syrtis_soup.find("h2", class_='title').get_text()
    syrtis_sample=browser.links.find_by_partial_text('Sample')
    syrtis_sample.click()
    # Find the relative image url
    syrtis_url_rel=img_soup.select_one('img.wide-image').get('src')
    # Use the base URL to create an absolute URL
    syrtis_img_url=f'https://astrogeology.usgs.gov{syrtis_url_rel}'

    try:
        syrtis_title=syrtis_soup.find("h2", class_='title').get_text()
        syrtis_url_rel=img_soup.select_one('img.wide-image').get('src')

    except AttributeError:
        return None, None

    return syrtis_img_url, syrtis_title

# Function for Valles Marineris Hemisphere
def valles(browser):

    # Visit Valles Marineris URL
    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Find and click the Hemisphere link
    valles_image=browser.find_by_text('Valles Marineris Hemisphere Enhanced')
    valles_image.click()
    # Parse the resulting html with soup
    html=browser.html
    img_soup=BeautifulSoup(html, 'html.parser')
    valles_soup=BeautifulSoup(html, 'html.parser')
    # Find title
    valles_title=valles_soup.find("h2", class_='title').get_text()
    valles_sample=browser.links.find_by_partial_text('Sample')
    valles_sample.click()
    # Find the relative image url
    valles_url_rel=img_soup.select_one('img.wide-image').get('src')
    valles_img_url=f'https://astrogeology.usgs.gov{valles_url_rel}'

    try:
        valles_title=valles_soup.find("h2", class_='title').get_text()
        valles_url_rel=img_soup.select_one('img.wide-image').get('src')

    except AttributeError:
        return None, None
    
    return valles_img_url, valles_title

if __name__=='__main__':
    # If running as script, print scraped data
    print(scrape_all())