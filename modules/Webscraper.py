from selenium import webdriver
import bs4
import json
import requests
import re

from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Webscraper:

    def __init__(self, url):
        self.url = url
        

    
    def search(self, param):
      # headless is needed here because we do not have a GUI version of firefox
        options = Options()
        options.headless = True
      # driver = webdriver.Firefox(options=options, executable_path=r'/tmp/geckodriver')
        browser = webdriver.Firefox(options=options)
        browser.get(self.url)
        browser.implicitly_wait(2)
        
        #print(browser.find_elements_by_class_name('_2EO8yBlXG7 _2tkZlwrBKq _2kAQ9R14MS'))
        browser.find_elements_by_tag_name('button')[1].click()
        #print(browser.find_elements_by_link_text('Afvis alle'))
        #print(browser.find_element_by_xpath("//a[@href='/cl/37/Grafikkort?attr_50615361=56611824']"))    
        #link_to_nvidia = browser.find_elements_by_link_text("/cl/37/Grafikkort?attr_50615361=56611824")
        #print(link_to_nvidia)
        #link_to_nvidia[0].click()      
        browser.find_element_by_xpath("//a[@href='/cl/37/Grafikkort?attr_50615361=56611824']").click()
        browser.find_elements_by_class_name('_3kbvwJ4edH')[0].click()
        browser.implicitly_wait(2)
        string_url = browser.current_url
        print(string_url)
        req = requests.get(string_url)
        soup = bs4.BeautifulSoup(req.text, 'html.parser')
        #print(soup)
        #print(browser.find_elements_by_partial_link_text("/cl/37/Grafikkort?attr_50615361=56611824"))
        #print(browser.find_elements_by_id('Title'))   
        #button = browser.find_element_by_id('declineButton')
        #button.click()
        mydivs = soup.find_all("div", {"class": "_2Vdwcz_zWR _1bgVr-M90D"})
        #print(mydivs[0])
        #File_object = open(r"gpu_stuff.txt","w")
        #File_object.write(str(mydivs))
        #print( re.findall("^3060", "gpu_stuff.txt") )
        print(mydivs[0].find("title"))
        