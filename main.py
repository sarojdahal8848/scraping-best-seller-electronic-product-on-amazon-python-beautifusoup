
# Best Seller Electronic product on amazon
import requests
from bs4 import BeautifulSoup
import csv

page_number=1
try:
    with open('best_sell.csv','w',newline="") as csv_file:

        csv_write = csv.writer(csv_file)
        csv_write.writerow(['Rank','Title','Price','Rating'])
        for i in range(2):
            url = f'https://www.amazon.in/gp/bestsellers/electronics/ref=zg_bs_pg_2?ie=UTF8&pg={page_number}'

            header ={
                'user-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
            }

            content = requests.get(url,header).text
            soup = BeautifulSoup(content,'lxml')
            

            wrapper = soup.find('ol',id="zg-ordered-list")


            single = wrapper.find_all('li',class_="zg-item-immersion")

            for single in single:
                    
                # Finding title of the product
                title = single.find('span',class_="aok-inline-block zg-item").a.find_all('div')[1]
                title =title.text
                title = title.replace('\n',' ')
                title = title.strip()

                # Finding the rank
                rank = single.find('span',class_="zg-badge-text")
                rank = rank.text[1:]

                try:
                    #Finding the price of the product
                    price = single.find('span',class_="aok-inline-block zg-item").find('span',class_="p13n-sc-price")
                    price = price.text
                    price = price[2:]
                    price = price.replace(',','')
                except Exception as e:
                    print(e)
                

                #Finding the rating of the product

                rate = single.find('span',class_="aok-inline-block zg-item").i.text[0:3]
                csv_write.writerow([rank,title,price,rate])
            page_number += 1
except Exception as e:
    print(e)