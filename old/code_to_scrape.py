#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:02:50 2020

@author: eser
"""
from selenium import webdriver

import pandas as pd
from   selenium.common.exceptions import TimeoutException
speaker_names =['Tang, Mengxing']
browser = webdriver.Chrome()
h_index =[]
subject_list = []
for speaker in speaker_names:
    browser.get('https://scholar.google.de/citations?hl=de&user=6ps6CuwAAAAJ')
    box= browser.find_element_by_id("gs_hdr_sre")
    box.click()
    search_box = browser.find_element_by_id('gs_hdr_tsi')
    
    
    submit = browser.find_element_by_name('btnG')
    
    search_box.send_keys(speaker)
    
    submit.click()
    
    
    name = browser.find_element_by_class_name('gs_hlt')
    name.click()
    current = browser.find_element_by_class_name('gsc_prf_il')
    subjects = browser.find_element_by_id("gsc_prf_int")
    print(subjects.text)

    #table = browser.find_elements_by_class_name('gsc_rsb_std')
    #for number in table:
    #    print(number.text)
    #h_index.append(h_index_number.text)
    
#print(h_index)