from bs4 import BeautifulSoup
import requests

p1 = requests.get('https://www.t-nation.com/')
page = p1.content

soup1 = BeautifulSoup(page, 'html5lib')

soup1.findall('div', class_='leadImgWrap')