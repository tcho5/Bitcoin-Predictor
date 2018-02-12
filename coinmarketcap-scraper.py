import csv
import datetime
import urllib.request
from bs4 import BeautifulSoup

def createCSV():
    #Determing the current date and specially formatting it to pull data
    current_date = datetime.datetime.now()
    date_string = ""
    if(int(current_date.day) < 10):
        if(int(current_date.month) < 10): 
            #Both the day and the month need the preficing "0"
            rent_date_day = "0" + str(current_date.day)
            rent_date_month = "0" + str(current_date.month)
            date_string = str(current_date.year) + str(current_date.month) + str(current_date.day)
        else:
            #Just the current date needs a preficing "0"
            rent_date_day = "0" + str(current_date.day)
            date_string = str(current_date.year) + str(current_date.month) + str(current_date.day)
    else:
        if(int(current_date.month) < 10): 
            #Just the current month needs the preficing "0"
            rent_date_month = "0" + str(current_date.month)
            date_string = str(current_date.year) + str(current_date.month) + str(current_date.day)
        else:
            #The date requires no preficing "0"
            date_string = str(current_date.year) + str(current_date.month) + str(current_date.day)
    
    #Specifying the url that we want to scrape from. We use the date determined above 
    #	to ensure we pull information from the most recent date
    quote_page = 'https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=' + date_string 
    
    #Query the page and return the html
    page = urllib.request.urlopen(quote_page)
    #Parse using BeautifulSoup
    soup = BeautifulSoup(page, 'html.parser')
    
    #Write the header of the csv file
    with open('coinmarket.csv', 'w') as csv_file:
    	 writer = csv.writer(csv_file)
    	 writer.writerow(["DATE", "OPEN", "HIGH", "LOW", "CLOSE", "MARKET CAP"])
    csv_file.close()
    #Go through and parse the page by finding the "tr" tags with the attribute 
    #	class="text-right" 
    ctr = 0
    for tr in soup.find_all('tr', attrs={'class':'text-right'}):
        input_words = tr.text.split() # 9 Total elements in the list
        date = input_words[0] + " " + input_words[1] + " " + input_words[2] #Creates the date, month, year
        ctr += 1
        with open('coinmarket.csv', 'a') as csv_file: #Write each element back into the csv
            writer = csv.writer(csv_file)
            writer.writerow([date, input_words[3], input_words[4], input_words[5], input_words[6], input_words[8]])
                
    #print(ctr)
    csv_file.close()
    return ctr

