from splinter import Browser
from bs4 import BeautifulSoup
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    # NASA Mars News
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find('li', class_='slide')

    news_title = news.find('div', class_='content_title').text
    news_p = news.find('div', class_='article_teaser_body').text

    # JPL Mars Space Images - Featured Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    base_url = 'https://www.jpl.nasa.gov'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_relative_path = soup.find('ul', class_='articles').find('li', class_='slide').find('a')['data-fancybox-href']
    featured_image_url = base_url + featured_image_relative_path

    # Mars Weather
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_weather = soup.find('div', class_='ProfileTimeline').find('li').find('div', class_='content').find('p').text

    # Mars Facts
    import pandas as pd
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)

    df = tables[0]
    df.columns = ['description', 'value']
    df = df.set_index('description')
    fact_html = df.to_html()

    # Mars Hemispheres
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    base_url = 'https://astrogeology.usgs.gov'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', class_='result-list').find_all('div', class_='description')

    hemisphere_image_info = []
    for ind,item in enumerate(items):
        item_dict = {}
        item_dict['title'] = item.find('h3').text
        browser.find_by_tag('h3')[ind].click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        item_dict['img_url'] = base_url + soup.find('img', class_='wide-image')['src']
        hemisphere_image_info.append(item_dict)
        browser.back()

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "fact_html": fact_html,
        "hemisphere_image_info": hemisphere_image_info
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data