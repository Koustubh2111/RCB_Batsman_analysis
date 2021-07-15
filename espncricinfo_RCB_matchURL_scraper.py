# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 12:20:37 2021

@author: Owner
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option("prefs", 
{"profile.default_content_setting_values.notifications": 2 
 })
driver = webdriver.Chrome(options = options)
driver.get('https://www.espncricinfo.com/team/royal-challengers-bangalore-335970/match-results')

#Click on the month button
month_reset = driver.find_element_by_xpath('/html/body/div[1]/section/section/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/input')
month_reset.click()

###### PREP ############################
#list of number of clicks for each year
#2011, 12, 13, 14, 15, 16, 17, 18, 19, 20 , 21
num_clicks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#List x_paths for months played in each year
march = '#main-container > div:nth-child(1) > div > div.container > div > div.col-16.col-md-16.col-lg-12.main-content-x > div:nth-child(1) > div > div > div:nth-child(2) > div.card.content-block.filter-container > div.select-box--date-picker-button > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__month.react-datepicker__monthPicker > div:nth-child(1) > div.react-datepicker__month-text.react-datepicker__month-2'
april = '#main-container > div:nth-child(1) > div > div.container > div > div.col-16.col-md-16.col-lg-12.main-content-x > div:nth-child(1) > div > div > div:nth-child(2) > div.card.content-block.filter-container > div.select-box--date-picker-button > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__month.react-datepicker__monthPicker > div:nth-child(2) > div.react-datepicker__month-text.react-datepicker__month-3'
may = '#main-container > div:nth-child(1) > div > div.container > div > div.col-16.col-md-16.col-lg-12.main-content-x > div:nth-child(1) > div > div > div:nth-child(2) > div.card.content-block.filter-container > div.select-box--date-picker-button > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__month.react-datepicker__monthPicker > div:nth-child(2) > div.react-datepicker__month-text.react-datepicker__month-4'
sept = '#main-container > div:nth-child(1) > div > div.container > div > div.col-16.col-md-16.col-lg-12.main-content-x > div:nth-child(1) > div > div > div:nth-child(2) > div.card.content-block.filter-container > div.select-box--date-picker-button > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__month.react-datepicker__monthPicker > div:nth-child(3) > div.react-datepicker__month-text.react-datepicker__month-8'
octo = '#main-container > div:nth-child(1) > div > div.container > div > div.col-16.col-md-16.col-lg-12.main-content-x > div:nth-child(1) > div > div > div:nth-child(2) > div.card.content-block.filter-container > div.select-box--date-picker-button > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__month.react-datepicker__monthPicker > div:nth-child(4) > div.react-datepicker__month-text.react-datepicker__month-9'
nov = '#main-container > div:nth-child(1) > div > div.container > div > div.col-16.col-md-16.col-lg-12.main-content-x > div:nth-child(1) > div > div > div:nth-child(2) > div.card.content-block.filter-container > div.select-box--date-picker-button > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__month.react-datepicker__monthPicker > div:nth-child(4) > div.react-datepicker__month-text.react-datepicker__month-10'

month_css = [[april, may],                [april, may],                [april, may],                [april, may],                [april, may],                [april, may],                [april, may],                [april, may],                [march, april, may],                [sept, octo, nov],                 [april]]

############################################
all_year_list = []
#Navigate to year
for num, months in zip(num_clicks, month_css):
    year_url_list = []
    if num > 0:  

        #get left arrow
        larrow = button = driver.find_element_by_css_selector('#main-container > div:nth-child(1) > div > div.container > div > div.col-16.col-md-16.col-lg-12.main-content-x > div:nth-child(1) > div > div > div:nth-child(2) > div.card.content-block.filter-container > div.select-box--date-picker-button > div.react-datepicker__tab-loop > div.react-datepicker-popper > div > div > button.react-datepicker__navigation.react-datepicker__navigation--previous')

        #Click the left arrow "num" times
        for i in range(num):
            larrow.click()
    
    else:
        pass
        

    #navigate to first month, click on month again and navigate to next month
    for month in months:

        time.sleep(3)
        #Month 1
        #month is xpath        
        month_button = driver.find_element_by_css_selector(month)
        month_button.click()
        
        time.sleep(5)

        #get all matches 
        match_blocks = driver.find_elements_by_class_name('match-cta-container')

        #get the elemnents containing the url
        url_obj = [match_in_page.find_elements_by_tag_name('a')[0] for match_in_page in match_blocks]

        #extract url
        url = [u.get_attribute('href') for u in url_obj]
        
        #replace ball by ball commentary
        url = [u.replace('match-report', 'ball-by-ball-commentary') for u in url]

        #append to year url
        year_url_list.extend(url)

        #click on month again
        month_reset = driver.find_element_by_xpath('/html/body/div[1]/section/section/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/input')
        month_reset.click()

    #Once the months are done append to global list and reset to main page 
    all_year_list.append(year_url_list)

    driver.get('https://www.espncricinfo.com/team/royal-challengers-bangalore-335970/match-results')
    month_reset = driver.find_element_by_xpath('/html/body/div[1]/section/section/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/input')
    month_reset.click()
    
with open('BallToBall_Commentary_links.json', 'w') as f:
    json.dump(all_year_list, f)