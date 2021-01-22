#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:46:30 2020

@author: eser
"""

from selenium import webdriver

import pandas as pd

#potential speakers
directory= r'/home/eser/Downloads/python dosyalari/scraping_h_indexes/academics_list.xlsx'
speakers = pd.read_excel(directory)

data = pd.DataFrame(speakers)
data.columns = ['First Name', 'Last Name']								

last_names = data['Last Name']
first_names = data['First Name']

browser = webdriver.Chrome()

h_index =[]
i10_index = []
current = []
subjects = []
for i in range(len(last_names)):
    browser.get('https://www.scopus.com/freelookup/form/author.uri?zone=TopNavBar&origin=searchauthorfreelookup')
    
    search_last_name = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/form/div[1]/div/div[1]/div[1]/div/div/label')
    search_last_name.clear()
    search_first_name= browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/form/div[1]/div/div[1]/div[2]/div/div/label')
    search_first_name.clear()
    button = browser.find_element_by_id('authorSubmitBtn')
    
    search_last_name.send_keys(last_names[i])
    search_first_name.send_keys(first_names[i])
    button.click()
    
    try:
        name = browser.find_element_by_class_name('gs_hlt')
        name.click()
        table = browser.find_elements_by_class_name('gsc_rsb_std')
        list_of_table =[]
        for number in table:
            list_of_table.append(number.text)
        h_index.append(list_of_table[2])
        i10_index.append(list_of_table[4])
        
        current_scrape = browser.find_element_by_class_name('gsc_prf_il')
        current.append(current_scrape.text)
        
        subjects_list = browser.find_element_by_id("gsc_prf_int")
        subjects.append(subjects_list.text)
    except:
        h_index.append("not found")
        i10_index.append('not found')
        current.append('not found')
        subjects.append('not found')
        
        
print(h_index,i10_index,current)
data['H index'] = h_index
data['i10 Index'] = i10_index
data['Status and Current affiliation'] = current
data['Subject of speech'] = subjects
data.to_excel('with_h_index.xlsx')
#import ipdb; ipdb.set_trace()




