# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 16:14:45 2017

@author: wangq
"""

#https://www.idtdna.com/calc/analyzer
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

hp_driver = webdriver.Chrome()
hp_driver.get("https://www.idtdna.com/calc/analyzer")

gRNA_input = "AUGCAUGCAUGCAUGAUGAUCGAUCGAUCGA"  #Test value needs to be modified later


# The following is to find the text field and input sequence
gRNA_input_Xpath = "//textarea"
gRNA_input_Field = WebDriverWait(hp_driver,10).until(lambda hp_driver: hp_driver.find_element_by_xpath(gRNA_input_Xpath))
gRNA_input_Field.clear()
gRNA_input_Field.send_keys(gRNA_input)

# The following is to click the analyze button
gRNA_input_ID = "analyze-button"
analyze_button_element = WebDriverWait(hp_driver,10).until(lambda hp_driver: hp_driver.find_element_by_id(gRNA_input_ID))
analyze_button_element.click()
