from lxml import html
from bs4 import BeautifulSoup
import re

def parse_mhtml():
    mhtml = open("html/2012/Arizona.mhtml", 'rb')
    soup = BeautifulSoup(mhtml, features='lxml')
    quest = soup.find_all(name='div', attrs={"class": "ep_title"})
