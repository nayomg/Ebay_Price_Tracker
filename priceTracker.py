import requests
from bs4 import BeautifulSoup
import statistics as s

# url where we will extract data from

url = input("Please enter a url of a product you would like the average price of. ")
 

# link I used for testing-> "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1311&_nkw=apple+airpods+max&_sacat=0"


def getPrices(url):

    # names of tags that holds data of the objects to be listed
    #price = "s-item__price"

    # sends a request to the url for data
    response = requests.get(url)


    #parses the data into html only form (without styling), from here we can search for specific areas of data we need
    soup = BeautifulSoup(response.text,'html.parser')

    # searches for the areas of 'soup' where we will find the prices of the items we are looking for 
    results = soup.find("ul",{"class":"srp-results"}).find_all("li",{"class":"s-item"})

    prices = []

    #for loop to search for every price and add them to a list of prices which will be used later on
    for result in results:
        price_adder = result.find("span",{"class":"s-item__price"}).text
        if("to" in price_adder):
            continue
        else:

            # removes the $sign from the price and converts it to float form from string form and removes all commas
            price_adder = float(price_adder[1:].replace(",",""))
            prices.append(price_adder)

    
    return prices

prices = getPrices(url)
#returns average of all prices in the list
def getAVG(prices):
    return "Average Price of Product on this page is " , round(s.mean(prices),2)


print(getAVG(prices))