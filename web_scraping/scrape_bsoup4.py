# coding: utf-8

__author__ = ["Samuel Joshua"]

import bs4
import requests

# other recommended websites
# https://weather.gov
# https://xlcd.com

def getFlipkartPrice(requestUrl):
    res = requests.get(requestUrl)
    print(res.raise_for_status())

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # returns all values that match the below selector, since we gave a unique value, it has just one element
    # to get the below selector in Chrome, do inspect element -> in the window that comes select, right click on entire html around the price
    # then copy -> copy selector
    elems = soup.select('#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1')

    # text gives the content inside the selected HTML
    # returns a price 1,976
    # print(elems[0].text.strip())
    return elems[0].text.strip()


# pass the full url of the page you are searching for
price = getFlipkartPrice('https://www.flipkart.com/automate-boring-stuff-python/p/itmfc37mzsbxfnzh?pid=9781593275990&lid=LSTBOK9781593275990TYMZ9F&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=5fb1575b-9fdd-4e21-b191-5dc1cb137b35.9781593275990.SEARCH&ppt=sp&ppn=sp&ssid=f6rrmfacsg0000001585742394161&qH=2714065b80fb0e2f')
print("The Price " + price)

# old non function based code below
# res = requests.get('https://www.amazon.com/Microsoft-Surface-Intel-Core-256GB/dp/B07HZNKGDV?ref_=s9_apbd_orecs_hd_bw_b1LPqmx&pf_rd_r=7JJMVDX30TFDJ2FQZ8X6&pf_rd_p=5302a2c1-aa33-51f6-8451-a64a8e492a5c&pf_rd_s=merchandised-search-11&pf_rd_t=BROWSE&pf_rd_i=1232597011')
# res = requests.get('https://www.flipkart.com/automate-boring-stuff-python/p/itmfc37mzsbxfnzh?pid=9781593275990&lid=LSTBOK9781593275990TYMZ9F&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=5fb1575b-9fdd-4e21-b191-5dc1cb137b35.9781593275990.SEARCH&ppt=sp&ppn=sp&ssid=f6rrmfacsg0000001585742394161&qH=2714065b80fb0e2f')

# print(res.raise_for_status())

# soup = bs4.BeautifulSoup(res.text, 'html.parser')

# # returns all values that match the below selector, since we gave a unique value, it has just one element
# # to get the below selector, do inspect element -> in the window that comes select, right click on entire html around the price
# # then copy -> copy selector
# elems = soup.select('#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1')

# # text gives the content inside the selected HTML
# # returns a price 1,976
# print(elems[0].text.strip())