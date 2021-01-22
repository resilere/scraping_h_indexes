#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:46:30 2020

@author: eser
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

#potential speakers
directory= r'/home/eser/Downloads/python dosyalari/scraping_h_indexes/academics_list.xlsx'
speakers = pd.read_excel(directory)

data = pd.DataFrame(speakers)
data.columns = ['First Name', 'Last Name']								

last_names = data['Last Name']
first_names = data['First Name']

browser = webdriver.Chrome()

h_index_list =[]

affiliation_list = []

for i in range(len(last_names)):
    browser.get('https://www.scopus.com/freelookup/form/author.uri?zone=TopNavBar&origin=searchauthorfreelookup')
    
    
    
     
    try:
        search_last_name = browser.find_element_by_id('lastname')#search_last_name.clear()
        search_first_name= browser.find_element_by_id('firstname')#search_first_name.clear()
        browser.find_element_by_id('lastname').clear()
        browser.find_element_by_id('firstname').clear()
        button = browser.find_element_by_id('authorSubmitBtn')
            
        search_last_name.send_keys(last_names[i])
        search_first_name.send_keys(first_names[i])
        button.click()
            
        h_index = browser.find_element_by_class_name('dataCol4').text
        h_index_list.append(h_index)
        result = browser.find_element_by_class_name('docTitle')
        result.click()
        #import ipdb; ipdb.set_trace()
        affiliation = browser.find_element_by_class_name('link__text').text
        affiliation_list.append(affiliation)
    
    
    except:
        h_index_list.append("not found")
        
        affiliation_list.append('not found')
        
    browser.implicitly_wait(10)
    author_button = browser.find_element_by_class_name('gh-nav-action')
    author_button.click()
        
print(h_index_list,affiliation_list)
data['H index'] = h_index_list

data['Status and Current affiliation'] = affiliation_list

data.to_excel('from_scopus_with_h_index.xlsx')





