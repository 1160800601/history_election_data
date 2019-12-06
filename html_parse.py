from lxml import html
from bs4 import BeautifulSoup
import re


# line:
# questions_id, questions, num_responders, options, Dem_perc, Rep_perc, Other_perc, opt_perc, state
#
def parse_mhtml(path):
    mhtml = open(path, 'rb')
    soup = BeautifulSoup(mhtml, features='lxml')
    quest = soup.find_all(name='div', attrs={"class": "ep_title"})


parse_mhtml("html/2012/Arizona.mhtml")
