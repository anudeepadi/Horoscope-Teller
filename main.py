import urllib.request
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

def horoscope(sunsign):

        url = "https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/{}/".format(sunsign)
        
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
        res = requests.get(url,headers=headers)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        raw_data = soup.find("p",{"class":"margin-top-xs-0"})

        raw_date = soup.find("p",{"class":"orrange-text margin-bottom-0 margin-top-5 truncate-line"})

        print("Date : " + raw_date.text) 
        print("Your horscope {} says... {}".format(sunsign,raw_data.text))


sunsign = input("Enter Your Sunsign : ")
horoscope(sunsign)
