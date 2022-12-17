# AMAZON MULTIPAGE SCRAPPER
## A Multi-Page Scraper made with the help of Selenium and Beautiful Soup 🛒

![](https://media0.giphy.com/media/vgS9c8KaZacV6XIcm9/giphy.gif?cid=ecf05e47kz0lvja06pr9cg647dk8l5p3eaqh18lcpj33p31t&rid=giphy.gif&ct=s)

## Table of Contents

1.  [Overview](#Overview)
 
2.  [Libraries Used](#Libraries-Used)
3.  [Workflow](#Workflow)
4.  [Screenshots](#Screenshots)
5.  [Challenges](#Challenges)

## Overview

Selenium is an extremely powerful tool used for web data scraping however, it has some flaws that are fair because it was produced mainly to test web applications. On the other hand, BeautifulSoup was developed and produced for data scraping and it is extremely powerful indeed. However, even if BeautifulSoup has its faults, it won’t be beneficial if the required data is behind the “wall”, as it needs the user’s login for accessing the data or needs some actions from users. That’s where we can utilize Selenium, for automating user interactions through the website as well as we would use BeautifulSoup for scraping data.

I would be using BeautifulSoup and Selenium to extract product information like name, ratings, etc. from https://www.amazon.in/.

## Libraries-Used

-   `Selenium`
-   `BeautifulSoup`
-   `time`
-   `pandas`

## Workflow

- **Opening** Chrome browser and **accessing** https://www.amazon.in/ via Selenium.
- Getting the "Search Term" thourgh **user input**.
- **Formatting** the url to a dynamic url where "Search Term" can be changed.
- **Scraping** the *Product Names, Prices, Ratings, No. Of Items Sold and Link* for each of the products.
- **Navigating** to the next page using Selenium by clicking the next button automatically after the current page is being scraped.
- **Handling errors** like if some elements are not present (for example if reviews are not present) with try and catch block.
- **Converting** the scrapped data to .csv file using the `pandas` library.

Note:  I set the page limit to first 7 pages for scraping, you can increase it to scrap more pages.

## Screenshots

- Automatically scrapping each page one by one.
<br>
![](https://media0.giphy.com/media/9Tzi40JcZkijK38Frz/giphy.gif)

- The output .csv file.
<br>
![](https://media3.giphy.com/media/ZOBfxmH7B4sTb7GFIg/giphy.gif)


## Challenges
- There were some AttributeErrors so had to use try catch block to overcome it.
- I used Selenium for paginating through the next page so if we come over to the last page then there would be error as the "next page" button won't be there. I handeled it using try and catch block and a recursive function which will exit the scrapping after it reaches the last page.
- Scrapping in Amazon isn't allowed so had to use a `time` function and delayed the scraping with some seconds so that the site dosen't think that a bot is scraping,
- Scraping huge amount of data in Amazon might lead to an ip ban so I scraped the first 7 pages.

### Thankyou For Spending Your Precious Time Going Through This Project!
### If You Find Any Value In This Project Or Gained Something New Please Do Give A ⭐.
