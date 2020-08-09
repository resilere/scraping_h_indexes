#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:37:12 2020

@author: eser
"""

"""this is to scrape h index (and various  other information) from scopus"""

from selenium import webdriver
import pandas as pd


speakers = pd.read_excel(r'/home/eser/Downloads/Potential Speakers for QCI 2.xlsx')

data = pd.DataFrame(speakers, index = range(0,15))
data.columns = ['First Name','Last Name', 'Where I found',	'Status and Current affiliation',	'Previous Affiliations',	'H index',	'i10 Index'	,'Subjects of interest', 'Subject of speech',	'Comment',	'Contact'	]

browser = webdriver.Chrome()

browser.get('https://www.scopus.com/freelookup/form/author.uri?zone=TopNavBar&origin=searchauthorfreelookup')
lastname = data['Last Name']
print(lastname)
firstname = data['First Name']
h_index_list =[]
affiliation_list = []
subject_list = []
index = 0
for last_name in lastname:
     
    last_name_box= browser.find_element_by_id('lastname')
    first_name_box=browser.find_element_by_id('firstname')
    browser.find_element_by_id('lastname').clear()
    browser.find_element_by_id('firstname').clear()
    last_name_box.send_keys(last_name)
    first_name_box.send_keys(firstname[index])
    button = browser.find_element_by_id('authorSubmitBtn')
    button.click()
    try:
        
        h_index = browser.find_element_by_class_name('dataCol4').text
        h_index_list.append(h_index)
        browser.find_element_by_class_name('docTitle').click()
        
        affiliation = browser.find_element_by_id('firstAffiliationInHistory').text
        affiliation_list.append(affiliation)
        subject = browser.find_element_by_id('subjectAreaBadges').text
        subject_list.append(subject)
    except:
        h_index_list.append("not found")
        affiliation_list.append('not found')
        subject_list.append('not found')
    index += 1
    author_button = browser.find_element_by_id('gh-Author search')
    author_button.click()
    #print(affiliation_list, subject_list)
    
print(h_index_list,affiliation_list,subject_list)
new_data = pd.DataFrame(list(zip(lastname, firstname, h_index_list, affiliation_list, subject_list)), 
               columns =['last name', 'first name', 'h index', 'affiliation', 'subjects'])
new_data.to_excel('with_h_index3.xlsx')