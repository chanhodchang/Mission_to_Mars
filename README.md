# Mission_to_Mars
Using Web Scrapping to gather data and store it using MongoDB and displaying it onto a Flask app

## Project Overview
Used Web Scraping tools such as Splinter and BeautifulSoup through Python and Jupyter Notebook to scrape data from several Mars NASA webpages. The data scraped was then displayed in a Flask webpage which was designed by HTML5. 

The challenge project adds another four images onto the Flask site from a different NASA webpage. Data is scraped to grab the images of the different Mars hemispheres

## Resources
- Data Sources: https://mars.nasa.gov/news/, https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars, http://space-facts.com/mars/, https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
- Software: Python 3.6.1, conda 4.7.12, ChromeDriver 79.0.3945.16, Splinter 0.13.0, BeautifulSoup 4.8.1, MongoDB 4.2, Bootstrap 4.0

## Summary 

The project was to web scrape data from several NASA webpages. These webpages are scraping friendly, which is important when web scraping websites. The data that was grabbed from these websites were Mars articles, images, and a facts table. These data were then transfered to a Flask webpage which was created and edited with HTML. 

1. First wrote and tested code on Jupyter Notebook to see if web scraping was successful.
2. Transferred data into VS Code to be editted into a function.
3. Created four different functions to accomplish different web scraping tasks. 
4. Created a Flask app and coded different routes to connect the web scraping functions to app.py.
5. Conneceted MongoDB to the Flask app, so that data scraped from the webiste would be stored inside the database.
6. Wrote code from HTML to design the webpage for the Flask app.
7. Ran the app.py after connecting it to the HTML code.
8. Opened the Flask webpage and test ran the webscraping process.

## Analysis

Web Scraping is a powerful tool that can gather data from a website. It is especially useful when there is constant flow of new data. Webscraping can instantly gather the new data and update onto the desired databases. 