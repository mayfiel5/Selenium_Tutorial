"""

Using Selenium to Download Data from a Website
Data Source: https://fred.stlouisfed.org/
Selenium Library: http://robotframework.org/SeleniumLibrary/
Author: Brad Mayfield
"""
#%% Libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pandas as pd
import numpy as np

#%% Main Program
os.remove('C:\\Users\\bradm\\Downloads\\RSGCS.csv') #Remove original file so updated file can replace in location

PATH = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(PATH)
driver.get("https://fred.stlouisfed.org/series/RSGCS") #Open Page

time.sleep(2)

link = driver.find_element_by_id("download-button") #Click Download Button
link.click()

time.sleep(2)

link = driver.find_element_by_id("download-data-csv") #Click csv option
link.click()

time.sleep(2)

driver.close()

#%% upload data from downloads
os.chdir('C:\\Users\\bradm\\Downloads')
df = pd.read_csv('RSGCS.csv')
print(df)


#%%





