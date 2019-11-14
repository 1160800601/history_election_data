import requests
from lxml import html
from bs4 import BeautifulSoup
from urllib.request import urlopen
from ghost import Ghost, Session
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
STATES = ['national', 'arizona', 'california', 'colorado', 'florida',
          'georgia', 'illinois', 'indiana', 'iowa', 'kentucky',
          'maine', 'michigan', 'minnesota', 'missouri', 'nevada',
          'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina',
          'ohio', 'oregon', 'pennsylvania', 'south carolina', 'texas',
          'utah', 'virginia', 'washington', 'wisconsin']



def generate_url(state):
    url = "https://edition.cnn.com/election/2016/results/exit-polls/" + state + "/president"
    return url


def s1():
    page = requests.Session().get(generate_url(STATES[0]))
    tree = html.fromstring(page.text)
    result = tree.xpath('//select[@class="select__select"]//option/text()')
    print(result)


def s2():
    ari_url = 'https://edition.cnn.com/election/2016/results/exit-polls/arizona/president'
    html2 = urlopen(ari_url).read().decode('utf-8')
    soup2 = BeautifulSoup(html2, features='lxml')
    poll__cell = soup2.find_all('td', {"class": "exit-poll__cell"})
    for cell in poll__cell:
        print(cell.get_text())
    # print(soup2.head)


def run3():
    gh = Ghost()
    ss = Session(gh, display=True)

    count = 0
    location = 0
    ss.open('https://edition.cnn.com/election/2016/results/exit-polls/arizona/president')
    ss.wait_timeout()

    html3 = ss.content.encode('utf-8')
    patten = re.compile(r'<td class="exit-poll__cell">', re.M)


def s4():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    count4 = 0
    location4 = 0

    driver.get('https://edition.cnn.com/election/2016/results/exit-polls/arizona/president')

    driver.implicitly_wait(10)

    html4 = driver.page_source

    soup4 = BeautifulSoup(html4, features='lxml')
    poll__cell = soup4.find_all('td', {"class": "exit-poll__cell"})
    for cell in poll__cell:
        print(cell.get_text())



def parse_list(driver):
    divs = driver.find_elements_by_class_name('exit-poll__cell')
    print(divs)

s4()
