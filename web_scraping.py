from bs4 import BeautifulSoup
import requests, openpyxl

try:
   response=requests.get("https://en.wikipedia.org/wiki/List_of_best-selling_books")
   soup=BeautifulSoup(response.text,'html.parser')
   print(soup)
except Exception as e:
    print(e)