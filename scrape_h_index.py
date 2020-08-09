#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:46:30 2020

@author: eser
"""

from selenium import webdriver

import pandas as pd
from   selenium.common.exceptions import TimeoutException

#potential speakers
speakers = pd.read_excel(r'/home/eser/Downloads/Potential Speakers for QCI 2.xlsx')

data = pd.DataFrame(speakers, index = range(0,26))
data.columns = ['Potential Speaker',	'Where I found',	'Status and Current affiliation',	'Previous Affiliations',	'H index',	'i10 Index'	,'Subject of speech',	'Comment',	'Contact'	]
																		

speaker_names = data['Potential Speaker']


browser = webdriver.Chrome()

h_index =[]
i10_index = []
current = []
subjects = []
for speaker in speaker_names:
    browser.get('https://scholar.google.de/citations?hl=de&user=6ps6CuwAAAAJ')
    box= browser.find_element_by_id("gs_hdr_sre")
    box.click()
    search_box = browser.find_element_by_id('gs_hdr_tsi')
    
    
    submit = browser.find_element_by_name('btnG')
    
    search_box.send_keys(speaker)
    
    submit.click()
    
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




