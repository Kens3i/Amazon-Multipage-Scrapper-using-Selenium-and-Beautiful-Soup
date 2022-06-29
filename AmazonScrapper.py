#Developed By Kens

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import pandas as pd

#opening chrome and accessing the link
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#formatting the url so that we could get according to the search term
inpu= input("Enter Term To Search: ")
template= "https://www.amazon.in/s?k={}"
url=template.format(inpu)

#maximizing the window so that the classes don't change
driver.maximize_window()
#Opening the url
driver.get(url)

#these arrays will store all the information
product_titles=[]
prices=[]
ratings=[]
items_sold_arr=[]
item_urls=[]

#this function is for finding the data from the web page and then scrape the data
def extract_record(results):

    for result in results:
        product_title = result.find("span", {"class": "a-size-medium a-color-base a-text-normal"}).text
        product_titles.append(product_title)

        try:
            price = result.find("span", {"class": "a-price-whole"}).text
        except AttributeError:
            price=""
        prices.append(price)

        try:
            rating = result.find("span", {"class": "a-icon-alt"}).text
        except AttributeError:
            rating=""
        ratings.append(rating)

        try:
            items_sold = result.find("span", {"class": "a-size-base s-underline-text"}).text
        except AttributeError:
            items_sold=""
        items_sold_arr.append(items_sold)

        #uncomment this for getting the discount
        # prev_price = result.find_all("span", {"class": "a-offscreen"})[1].text
        #
        # price_int = int(price.replace(",", "").replace("₹", ""))
        # prev_price_int = int(prev_price.replace(",", "").replace("₹", ""))
        # discount = ((prev_price_int - price_int) / prev_price_int) * 100
        # discount_final = str(discount)[:2] + "%"
        # discounts.append(discount_final)

        item_url = result.find("a", {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}).get("href")
        item_url = "https://www.amazon.in/" + item_url
        item_urls.append(item_url)

#for traversing through pages this is a recursive array
#initialized a page limit cuz I don't want to get banned by Amazon :")
def pages(page_limit):

    #will break the loop if page limit exceeds or if the "next page" button at th end doesn't exists
    while True:
        #this works on the current page which is opened by the driver
        soup = BeautifulSoup(driver.page_source, "html.parser")
        results = soup.find_all("div", {"data-component-type": "s-search-result"})
        time.sleep(2)
        extract_record(results)

        #clicking the "next page" button and looping again (recursive function)
        try:
            next_page = driver.find_element_by_css_selector('a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator')
            next_page.click()
            pages(page_limit)
        except NoSuchElementException:
            break

        if page_limit>=7:
            break
        else:
            page_limit+=1

#we start from page 0 to page 6
pages(0)

#converting data to dataframe and then to csv
amazon_df=pd.DataFrame({"Product Name":product_titles, "Price":prices, "Rating":ratings, "No. Of Items Sold":items_sold_arr, "Link":item_urls})
print(amazon_df)
amazon_df.to_csv('ScrappedData.csv', index=False)

#Subscribe to "Learn with Kens"