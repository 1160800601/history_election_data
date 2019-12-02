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

    driver.get('https://edition.cnn.com/election/2016/results/exit-polls/arizona/president')

    driver.implicitly_wait(10)

    html4 = driver.page_source

    soup4 = BeautifulSoup(html4, features='lxml')

    poll__cell = soup4.find_all('td', {"class": "exit-poll__cell"})
    poll__cell_array = []
    for cell in poll__cell:
        poll__cell_array.append(cell.get_text())

    questions = soup4.find_all('h3', {"class": "exit-poll__question"})
    questions_array = []
    for question in questions:
        questions_array.append(question.get_text())

    headers = soup4.find_all('th', {"class": "exit-poll__cell--header"})
    headers_array = []
    for header in headers:
        headers_array.append(header.get_text())

    answers = soup4.find_all('td', {"class": "exit-poll__cell exit-poll__cell--answer"})
    answers_array = []
    for answer in answers:
        answers_array.append(answer.get_text())

    for cell in poll__cell:
        print(cell.get_text())

def save_html(url, filename):
    driver = webdriver.Chrome()
    driver.get(url)
    page = input("input")
    html = driver.page_source
    with open("html/"+filename+'.html', 'a', encoding='utf-8') as f:
        f.write(html)


def s5():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://edition.cnn.com/election/2012/results/race/president/#exit-polls')
    driver.implicitly_wait(10)

    html4 = driver.page_source

    soup4 = BeautifulSoup(html4, features='lxml')

    question_titles = soup4.find_all(name='div', attrs={"class": "ep_title"})
    question_titles_array = []
    for quest_title in question_titles:
        question_titles_array.append(quest_title.get_text())
    print(question_titles_array)

def s6():
    html6 = open("html/2012/2012_national.html", 'rb')
    soup6 = BeautifulSoup(html6, features='lxml')

    question_titles = soup6.find_all(name='div', attrs={"class": "ep_title"})
    question_titles_array = []
    for quest_title in question_titles:
        question_titles_array.append(quest_title.get_text())
    print(question_titles_array)

def s7():
    file_name = "2008_nation"
    for i in range(1, 8):
        url = "https://edition.cnn.com/ELECTION/2008/results/polls/#val=USP00p" + str(i)
        save_html(url, file_name)

def s8():
    html8 = open("html/2008_nation.html", 'rb')
    soup8 = BeautifulSoup(html8, features='lxml')
    quest = soup8.find_all(name='div', attrs={"class": "cnnElex_pageLSubT"})

def s9():
    html9 = open("html/FL_EP_2012.mhtml", 'rb')
    soup9 = BeautifulSoup(html9, features='lxml')
    quest9 = soup9.find_all(name='div', attrs={"class": "ep_title"})
    print("1")

# https://blog.csdn.net/oChangWen/article/details/51959754
def parse_list(driver):
    divs = driver.find_elements_by_class_name('exit-poll__cell')
    print(divs)

s9()
